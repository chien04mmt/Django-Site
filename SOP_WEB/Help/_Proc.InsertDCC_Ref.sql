-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Vũ Văn Chiến CNCS>
-- Create date: <10.05.2022>
-- Description:	Thực hiện chức năng cấp mã DCC
-- =============================================
CREATE PROCEDURE  InsertDCC_Ref
( 
	 @DocNo as nvarchar(50) ,
	 @DocName as nvarchar(50) ,
	 @CreatedBy as nvarchar(50) ,
	 @CodeDocument as nvarchar(50) 	
) AS
BEGIN
	-- Lấy thông tin Id của Docref
	Declare  @ID_DocumentRef as nvarchar(50) =''
	Select  @ID_DocumentRef =ID FROM DocumentRef WHERE CodeDocument=@CodeDocument
	--Lấy số Order
	Declare @OrderBy as int=0
	Select  @OrderBy =OrderBy FROM DCC_Ref WHERE CodeDocument=@CodeDocument
	set @OrderBy=@OrderBy+1
	--Chèn thông tin vào bảng DCC đã cấp mã
	insert into DCC_Ref(ID,DocNo,DocName,CreatedBy,CreatedDate,IsDeleted,Status,CodeDocument,OrderBy,ID_DocumentRef)
	values(NEWID(), @DocNo, @DocName, @CreatedBy, GETDATE(), 0, '1', @CodeDocument, @OrderBy,@ID_DocumentRef)
		--Lấy thông tin đã chèn
	SELECT * FROM DCC_Ref WHERE CodeDocument=@CodeDocument
END
GO


             
