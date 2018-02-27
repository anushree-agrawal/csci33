import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("people.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for f_name, l_name, height, weight, eye_color in reader:
            db.execute("INSERT INTO people (first_name, last_name, height, weight, eye_color) VALUES (:first_name, :last_name, :height, :weight, :eye_color)",
                    {"first_name": f_name, "last_name": l_name, "height": float(height), "weight": int(weight), "eye_color": eye_color})
        db.commit()
if __name__ == "__main__":
    main()

