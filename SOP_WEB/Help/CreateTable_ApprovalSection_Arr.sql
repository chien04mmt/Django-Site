USE [SOP_V2]
GO

/****** Object:  Table [dbo].[ApprovalSection_Arr]    Script Date: 10/05/2022 16:48:13 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[ApprovalSection_Arr](
	[ID] [uniqueidentifier] NOT NULL,
	[CodeDocument] [varchar](50) NULL,
	[UserName] [varchar](50) NULL,
	[Station] [nvarchar](150) NULL,
	[Orders] [nvarchar](3) NULL,
	[IsCheck] [varchar](20) NULL,
	[Status] [varchar](20) NULL,
	[Time] [datetime] NULL,
	[Comment] [nvarchar](250) NULL,
	[CreatedBy] [varchar](50) NULL,
	[CreatedDate] [datetime] NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[ApprovalSection_Arr] ADD  CONSTRAINT [DF_ApprovalSection_Arr_Status]  DEFAULT ('') FOR [Status]
GO


