USE [SOP_V2]
GO

/****** Object:  Table [dbo].[RegisterDocumentArrive]    Script Date: 10/05/2022 16:48:58 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[RegisterDocumentArrive](
	[ID] [uniqueidentifier] NOT NULL,
	[Loaicongvan] [varchar](50) NULL,
	[Sodon] [varchar](50) NULL,
	[Nguoitrinhdon] [varchar](50) NULL,
	[Ngaynhanvankien] [datetime] NULL,
	[Sobiennhan] [varchar](50) NULL,
	[NgaytrinhkyGD] [datetime] NULL,
	[Sovankien] [varchar](50) NULL,
	[Noidungcongvan] [varchar](50) NULL,
	[Donvichusu] [varchar](50) NULL,
	[Donvihopban] [varchar](50) NULL,
	[Vanbanphuluc] [varchar](50) NULL,
	[Ghichu] [varchar](50) NULL,
	[Chondvkhac] [varchar](50) NULL,
	[Donvikhac] [varchar](50) NULL,
	[TepscanPDF] [varchar](50) NULL,
	[Tepvbtraloi] [varchar](50) NULL,
	[Dongsauhop] [varchar](50) NULL,
	[Traloivanban] [varchar](50) NULL,
	[Thoigianxuly] [datetime] NULL,
	[Ykienkhac] [varchar](50) NULL,
	[Status] [varchar](50) NULL,
	[Next_appro] [varchar](15) NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


