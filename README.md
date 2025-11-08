Database Design

The system uses three relational tables: STUDENT, COURSE, and GRADE.

STUDENT	(Stores student details)

COURSE	(Stores available courses)

GRADE	(Stores student grades for courses (linked by foreign keys))

Entity relational diagram
<img width="1844" height="1484" alt="image" src="https://github.com/user-attachments/assets/4eb27040-82cb-4b09-8d3d-4332b8ca58e0" />

One student can have many grades.

One course can also have many grades.

The GRADE table acts as a linking table (many-to-many relationship).

CRUD operations used - CREATE | READ | UPDATE | DELETE


<img width="373" height="725" alt="image" src="https://github.com/user-attachments/assets/75bd23df-7a58-4e53-9222-f95e75525b56" />


<img width="535" height="437" alt="image" src="https://github.com/user-attachments/assets/7e12c0d5-274a-446d-9df5-a8fe8d8be2f6" />


<img width="507" height="345" alt="image" src="https://github.com/user-attachments/assets/de11449f-5a97-4508-b928-0d95f2e80246" />


<img width="423" height="397" alt="image" src="https://github.com/user-attachments/assets/bdaffbab-b15b-4ba2-a00a-d00e53bb8eff" />


<img width="707" height="921" alt="image" src="https://github.com/user-attachments/assets/90637288-93d8-410d-8aa1-f5ad7129097f" />

