from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(tags= ['Vote'])

@router.post("/vote/", status_code = status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_id_check = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post_id_check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {vote.post_id} does not exist")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"User {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(user_id = current_user.id, post_id = vote.post_id)
        db.add(new_vote)
        db.commit()
        return {"message" : "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully deleted vote"}
    
