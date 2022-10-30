# We Help boot camp week 5 Task

## Require 3
`
3-1
`
>使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

```sql
insert into member (name, username, password)
values ('test', 'test', 'test');
insert into member (name, username, password)
values ('Armin', 'Armin', 'Arlert');
insert into member (name, username, password)
values ('Reiner', 'Reiner', 'Braun');
insert into member (name, username, password)
values ('Bertholdt', 'Bertholdt', 'Hoover');
insert into member (name, username, password)
values ('Annie', 'Annie', 'Leonhart');
```
![Require3_1](/Stage1_Week5/image/Require3_1.png)

`
3-2
`
>使用 SELECT 指令取得所有在 member 資料表中的會員資料。
```sql
select * from member;
```
![Require3_2](/Stage1_Week5/image/Require3_2.png)

`
3-3
`
>使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```sql
select * from member by time desc;
```
![Require3_3](/Stage1_Week5/image/Require3_3.png)

#### 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
```sql
select * from member by time desc limit 1,3;
```
![Require3_4](/Stage1_Week5/image/Require3_4.png)

`
3-4
`
>使用 SELECT 指令取得欄位 username 是 test 的會員資料。
```sql
select * from member where username='test';
```
![Require3_5](/Stage1_Week5/image/Require3_5.png)

`
3-5
`
>使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```sql
select * from member where username='test' and password='test';
```
![Require3_6](/Stage1_Week5/image/Require3_6.png)

`
3-6
`
>使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```sql
update member set name='test2' where username='test';
```
![Require3_7](/Stage1_Week5/image/Require3_7.png)

## Require 4

`
4-1
`
>取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```sql
select count(id) from member;
```
![Require4_1](/Stage1_Week5/image/Require4_1.png)

`
4-2
`
>取得 member 資料表中，所有會員 follower_count 欄位的總和。
```sql
select sum(follow_count) from member;
```
![Require4_2](/Stage1_Week5/image/Require4_2.png)

`
4-3
`
>取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```sql
select avg(follow_count) from member;
```
![Require4_3](/Stage1_Week5/image/Require4_3.png)


## Require 5

`
5-1
`
>使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
```sql
select member.name, message.content from member
inner join message on member.id=message.member_id;
```
![Require5_1](/Stage1_Week5/image/Require5_1.png)

`
5-2
`
>使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
```sql
select member.name, message.content from member
inner join message on member.id=message.member_id
where member.username='test';
```
![Require5_2](/Stage1_Week5/image/Require5_2.png)

`
5-3
`
>使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
```sql
select ave(like_count) from member
inner join member on message.member_id=member.id
where member.username='test';
```
![Require5_3](/Stage1_Week5/image/Require5_3.png)
