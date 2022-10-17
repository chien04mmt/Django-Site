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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_ApproOrCancelApprovalSection]
(
@CodeDocument varchar(50),
@Comment varchar(500),
@States varchar(20),
@User varchar(50),
@Action varchar(50)
)
as
begin
	declare @sql as nvarchar(max)
	declare @TableName nvarchar(500)
	declare @ColName nvarchar(500)
	declare @Status nvarchar(50)
	
	
	--Thao tác ký đơn
	if @Action='APPRO'	begin set @Status='C-00010'	end
	
	--Thao tác hủy đơn
	if (@Action='CANCEL') begin set @Status='C-00011' end
	
	
	--Thưc hiện cập nhật tình trạng ký hoặc hủy đơn	
	set @sql=''
	if @CodeDocument like '%SOP-A%' begin set @TableName=' RegisterCodeDocument' set @States='A'+SUBSTRING(@States,2,2) set @ColName='CodeDocument' end
	if @CodeDocument like '%SOP-B%' begin set @TableName=' RegisterEditDocument' set @States='B'+SUBSTRING(@States,2,2) set @ColName='EditDocument' end
	if @CodeDocument like '%SOP-C%' begin set @TableName=' RegisterPublishDocument' set @States='C'+SUBSTRING(@States,2,2) set @ColName='PublishDocument' end
	if @CodeDocument like '%SOP-D%' begin set @TableName=' ApplicationObsoletedDocument' set @States='D'+SUBSTRING(@States,2,2) set @ColName='ObsoletedDocument' end
	if @CodeDocument like '%SOP-G%' begin set @TableName=' RegisterCancelDocument' set @States='G'+SUBSTRING(@States,2,2) set @ColName='CancelDocument' end			
	
	-- Cập nhật trạng thái  ký cho bảng lưu trình ký
	UPDATE [ApprovalSection]
			SET Comment=@Comment,Status='C-00011',UpdatedDate=GETDATE(),UpdatedBy=@User
			WHERE CodeDocument=@CodeDocument and UserName=@User
	        
	-- Cập nhật State cho đơn theo bảng của mỗi loại đơn
	set @sql+=N'UPDATE'+ @TableName +'
			SET States ='''+@States+''',UpdatedBy='''+@User+''',UpdatedDate=GETDATE() 
			WHERE '+@ColName+' ='''+@CodeDocument+''''
		print(@sql)
	exec(@sql)

	
end
-- exec sp_ApproOrCancelApprovalSection 'SOP-G-V202200071','@Comment','A01','V0515000','CANCEL'







