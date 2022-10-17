-- ================================================
-- Insert Document Ref
-- ================================================
Use SOP_V2
Go
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<V0515000,,Chiến CNCSIT>
-- Create date: <11.08.2022,,>
-- Description:	<Coder,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_InsertDocRef](
	@CodeDocument varchar(50),	
	@DocumentName nvarchar(250),
	@FileName nvarchar(250),
	@EstimatedCloseDate datetime,
	@Createdby nvarchar(50),
	@OrderBy int
)
as
begin
declare @AssignedRevisor nvarchar(250)
set @AssignedRevisor =''

insert into DocumentRef
(ID,
DocumentName,
FileName,
AssignedRevisor,
EstimatedCloseDate,
CreatedDate,
Createdby,
CodeDocument,
OrderBy) 
values(NEWID(), @DocumentName, @FileName, @AssignedRevisor, 
		@EstimatedCloseDate, GETDATE(), @Createdby, 
		@CodeDocument, @OrderBy)              
                
end
GO
-- exec sp_InsertDocRef '@CodeDocument','@DocumentName','@FileName',
-- '@Createdby','@OrderBy'

