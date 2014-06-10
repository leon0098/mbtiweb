insert into paper_paper (name) values('p1');
insert into paper_question (serialno,content,paper_id) values('1','q1',1);
insert into paper_question (serialno,content,paper_id) values('2','q2',1);
insert into paper_option (serialno,content,question_id) values('a','o1',1);
insert into paper_option (serialno,content,question_id) values('b','o2',1);
insert into paper_option (serialno,content,question_id) values('c','o3',1);
insert into paper_answer (question_id,option_id) values('1','2');

select * from paper_paper
select * from paper_question
select * from paper_option
select * from paper_answer

delete from paper_paper
select from paper_question
select from paper_option
select from paper_answer
