import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("yelp.csv") as f:
        insertions = 0
        reader = csv.reader(f)
        next(reader)
        for name, pc, stars, rv_ct, categories in reader:
            db.execute("INSERT INTO yelp (name, postal_code, stars, review_count, categories) VALUES (:name, :postal_code, :stars, :review_count, :categories)",
                    {"name": name, "postal_code": pc, "stars": float(stars), "review_count": int(rv_ct), "categories": categories})
            insertions += 1
            print("Added %d businesses into table Yelp." % insertions)
        db.commit()
if __name__ == "__main__":
    main()
