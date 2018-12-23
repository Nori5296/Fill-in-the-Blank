-- Project Name : anaume
-- Date/Time    : 2018/12/08 10:28:56
-- Author       : nannd
-- RDBMS Type   : PostgreSQL
-- Application  : A5:SQL Mk-2

/*
  BackupToTempTable, RestoreFromTempTable�^�����߂��t������Ă��܂��B
  ����ɂ��Adrop table, create table ����f�[�^���c��܂��B
  ���̋@�\�͈ꎞ�I�� $$TableName �̂悤�Ȉꎞ�e�[�u�����쐬���܂��B
*/

-- ��蕶����
--* RestoreFromTempTable
create table fillquestion_detail (
  fillquestion_id integer not null
  , string_no integer not null
  , text varchar not null
  , answer_text varchar
  , constraint fillquestion_detail_PKC primary key (fillquestion_id,string_no)
) ;

-- ��蕶
--* RestoreFromTempTable
create table fillquestions (
  fillquestion_id integer not null
  , original_text_id integer not null
  , fillquestion_name varchar not null
  , registed_on timestamp not null
  , regist_user integer not null
  , updated_on timestamp not null
  , update_user integer not null
  , constraint fillquestions_PKC primary key (fillquestion_id)
) ;

-- ����
--* RestoreFromTempTable
create table original_texts (
  original_text_id integer not null
  , original_text text not null
  , registed_on timestamp not null
  , regist_user integer not null
  , updated_on timestamp not null
  , update_user integer not null
  , constraint original_texts_PKC primary key (original_text_id)
) ;

alter table fillquestion_detail
  add constraint fillquestion_detail_FK1 foreign key (fillquestion_id) references fillquestions(fillquestion_id);

alter table fillquestions
  add constraint fillquestions_FK1 foreign key (original_text_id) references original_texts(original_text_id);

comment on table fillquestion_detail is '��蕶����';
comment on column fillquestion_detail.fillquestion_id is '��蕶ID';
comment on column fillquestion_detail.string_no is '������ԍ�';
comment on column fillquestion_detail.text is '������';
comment on column fillquestion_detail.answer_text is '���𕶎���';

comment on table fillquestions is '��蕶';
comment on column fillquestions.fillquestion_id is '��蕶ID';
comment on column fillquestions.original_text_id is '����ID';
comment on column fillquestions.fillquestion_name is '��蕶����';
comment on column fillquestions.registed_on is '�o�^����';
comment on column fillquestions.regist_user is '�o�^��';
comment on column fillquestions.updated_on is '�X�V����';
comment on column fillquestions.update_user is '�X�V��';

comment on table original_texts is '����';
comment on column original_texts.original_text_id is '����ID';
comment on column original_texts.original_text is '����';
comment on column original_texts.registed_on is '�o�^����';
comment on column original_texts.regist_user is '�o�^��';
comment on column original_texts.updated_on is '�X�V����';
comment on column original_texts.update_user is '�X�V��';

