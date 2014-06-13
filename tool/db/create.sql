insert into paper_paper (id,name,description) values (1.0,'试卷1','试卷1');
insert into paper_question (id,serialno,content,paper_id) values (1.0,1.0,'认识你的人倾向形容你为： ',1.0);
insert into paper_question (id,serialno,content,paper_id) values (2.0,2.0,'下列哪一件事听起来比较吸引你？ ',1.0);
insert into paper_option (id,serialno,content,type,question_id) values (1.0,'A','热情和敏感。','F',1.0);
insert into paper_option (id,serialno,content,type,question_id) values (2.0,'B','逻辑和明确。','T',1.0);
insert into paper_option (id,serialno,content,type,question_id) values (3.0,'A','与情人到有很多人且社交活动频繁的地方。','E',2.0);
insert into paper_option (id,serialno,content,type,question_id) values (4.0,'B','呆在家中与情人做一些特别的事情，例如说观赏一部有趣的录影带并享用你最喜欢的外卖食物。','I',2.0);
insert into paper_answer (id,description,question_id,option_id) values (1.0,'题目1答案',1.0,1.0);
insert into paper_answer (id,description,question_id,option_id) values (2.0,'题目2答案',2.0,3.0);
