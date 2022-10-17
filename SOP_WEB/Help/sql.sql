  
--Cập nhật dữ liệu Từ bảng sang bảng bằng CurSor
SET NOCOUNT ON;  
DECLARE vend_cursor CURSOR FOR 
	SELECT r.DocNo,r.IsDeleted FROM [SOP].[dbo].[Doc_detail] as d
  INNER JOIN [SOP].[dbo].[RegisterPublishDocument] as r ON d.DocNo=r.DocNo
OPEN vend_cursor  

DECLARE @DocNo varchar(50);
DECLARE @IsDeleted nchar(2);

Fetch Next From vend_cursor  INTO @DocNo,@IsDeleted
While @@Fetch_Status = 0
Begin
	Update [SOP].[dbo].[Doc_detail] set IsDeleted = @IsDeleted Where DocNo=@DocNo
	Fetch Next From vend_cursor  INTO @DocNo,@IsDeleted
End

CLOSE vend_cursor;
DEALLOCATE vend_cursor; 





   
--Cập nhật ID từ bảng DCC đồng bộ với DcRef
SET NOCOUNT ON;  
DECLARE vend_cursor CURSOR FOR 
	  SELECT df.ID1,dcc.[ID_DocumentRef] 
		  FROM [SOP].[dbo].[DocumentRef] as df
		  INNER JOIN  [SOP].[dbo].[DCC_Ref] as dcc on dcc.[ID_DocumentRef]=df.ID
OPEN vend_cursor  

DECLARE @ID1 varchar(50);
DECLARE @ID_DocumentRef varchar(50);

Fetch Next From vend_cursor  INTO @ID1,@ID_DocumentRef
While @@Fetch_Status = 0
Begin
	Update [SOP].[dbo].[DCC_Ref] set [ID_DocumentRef1] = @ID1 Where ID_DocumentRef=@ID_DocumentRef
	Fetch Next From vend_cursor  INTO  @ID1,@ID_DocumentRef
End

CLOSE vend_cursor;
DEALLOCATE vend_cursor; 

-- Lấy danh sách các bảng
  SELECT r.*,d.* 
  FROM [SOP].[dbo].[DCC_Ref] as r
  INNER JOIN [SOP].[dbo].[Doc_detail] as d on r.DocNo=d.DocNo


  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT d.*,cg.Name,c1.Name as States1,e.DocumentName,
  FROM [SOP].[dbo].[Doc_detail] as d

  left JOIN [SOP].[dbo].[RegisterEditDocument] as e on e.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterCancelDocument] as c on c.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterPublishDocument] as p on p.DocNo=d.DocNo
  
  left outer JOIN SOP.dbo.CategoryType as cg on d.Type=cg.Code 
  left outer JOIN SOP.dbo.CategoryType as c1 on d.States=c1.Code 
  WHERE d.IsDeleted='0'
  Order by d.CreatedDate desc


/****** Script for SelectTopNRows command from SSMS  ******/
SELECT d.*,e.DocumentName,c.Doc
  FROM [SOP].[dbo].[Doc_detail] as d
  left JOIN [SOP].[dbo].[RegisterEditDocument] as e on e.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterCancelDocument] as c on c.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterPublishDocument] as p on p.DocNo=d.DocNo
  WHERE d.IsDeleted='0'
  Order by d.CreatedDate desc




-- Tra cứu thông tin đầu đơn
  SELECT d.*,cg.Name,c1.Name as States1,dcc.CodeDoc as CodeDoc1,dcc.DocName as DocName1
  FROM [SOP].[dbo].[Doc_detail] as d

  left JOIN [SOP].[dbo].[RegisterEditDocument] as e on e.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterCancelDocument] as c on c.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterPublishDocument] as p on p.DocNo=d.DocNo
   LEFT JOIN [SOP].[dbo].[DCC_Ref] as dcc on dcc.DocNo=d.DocNo 
   
  left outer JOIN SOP.dbo.CategoryType as cg on d.Type=cg.Code 
  left outer JOIN SOP.dbo.CategoryType as c1 on d.States=c1.Code 
  
  WHERE d.IsDeleted='0'
  Order by d.CreatedDate desc


    -- Lấy danh sách văn bản
  
  SELECT d.*,cg.Name as Type1,c1.Name as States1,dcc.CodeDoc as CodeDoc1,dcc.DocName as DocName1,de.Rev,dp.Name as Department1
  FROM [SOP].[dbo].[Doc_detail] as d

  left JOIN [SOP].[dbo].[RegisterEditDocument] as e on e.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterCancelDocument] as c on c.DocNo=d.DocNo
  left JOIN [SOP].[dbo].[RegisterPublishDocument] as p on p.DocNo=d.DocNo
   LEFT JOIN [SOP].[dbo].[DCC_Ref] as dcc on dcc.DocNo=d.DocNo 
   
  left outer JOIN SOP.dbo.CategoryType as cg on d.Type=cg.Code 
  left outer JOIN SOP.dbo.CategoryType as c1 on d.States=c1.Code 
  left outer JOIN [SOP].[dbo].[RegisterPublishDocument] as de on dcc.CodeDoc=de.CodeNo
  left outer Join SOP.dbo.CategoryType as dp on dp.Code=d.Department
  
  WHERE d.IsDeleted='0'
  Order by d.CreatedDate desc