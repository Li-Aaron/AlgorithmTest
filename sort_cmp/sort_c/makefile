# Check Environment
!IFNDEF WORKSPACE
!ERROR WORKSPACE environmental variable not set
!ENDIF

!IFNDEF VCINSTALLDIR
# VS Path Define
VCINSTALLDIR		= D:\Program\Microsoft Visual Studio 14.0\VC
UniversalCRTSdkDir	= C:\Program Files (x86)\Windows Kits\10
NETFXSDKDir			= C:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1
PLATFORM 			= x64
PLATFORM_BIN		= amd64
# Tools define
MAKE				= nmake -nologo
CC					= "$(MSDEV_BIN_PATH)\cl"
LINK				= "$(MSDEV_BIN_PATH)\link"
!ELSE
MAKE				= nmake -nologo
CC					= cl
LINK				= link
!ENDIF

# Paths define
MSDEV_BASE = $(VCINSTALLDIR)
MSDEV_BIN_PATH = $(MSDEV_BASE)\bin\$(PLATFORM_BIN)
OUT_DIR = $(WORKSPACE)\Lib
SRC_DIR = $(WORKSPACE)\Src
INC_DIR = $(WORKSPACE)\Inc


# Lib define
!IFNDEF LIB
WDK_UCRT_LIB 	= $(UniversalCRTSdkDir)\lib\10.0.10240.0\ucrt\$(PLATFORM)
WDK_UM_LIB 		= $(UniversalCRTSdkDir)\lib\10.0.10240.0\um\$(PLATFORM)
WDK_NETFX_LIB 	= $(NETFXSDKDir)\lib\um\$(PLATFORM)
VC_LIB			= $(VCINSTALLDIR)\lib\$(PLATFORM_BIN)

LIBPATHS = /LIBPATH:"$(WDK_UCRT_LIB)" /LIBPATH:"$(WDK_UM_LIB)" /LIBPATH:"$(WDK_NETFX_LIB)" \
		/LIBPATH:"$(VC_LIB)"
!ENDIF

# Flags define
CFLAGS = /nologo /W3 /GS /GL /W3 /Gy /Zc:wchar_t /Zi /Gm- /O2 /sdl \
		/Zc:inline /fp:precise /D _WINDLL /D _MBCS \
		/WX- /Zc:forScope /Gd /Oi /MD /EHsc /I"$(INC_DIR)"

LFLAGS = $(LIBPATHS) /MANIFEST /LTCG:incremental /NXCOMPAT /DYNAMICBASE  /DEBUG /DLL /MACHINE:$(PLATFORM) /OPT:REF

OBJ = $(SRC_DIR)\sort_cmp.obj \
			$(SRC_DIR)\sort_bubble.obj \
			$(SRC_DIR)\sort_select.obj \
			$(SRC_DIR)\sort_insert.obj \
			$(SRC_DIR)\sort_shell.obj \
			$(SRC_DIR)\sort_quick.obj

TARGET_NAME = $(OUT_DIR)\sort.dll
PDB_NAME	= $(OUT_DIR)\sort.pdb


# Build Processes
all: $(TARGET_NAME)

$(TARGET_NAME): $(OBJ)
	$(LINK) /OUT:$(TARGET_NAME) /PDB:$(PDB_NAME) $(OBJ) $(LFLAGS) $(LIBS)

.c.obj:
	$(CC) $(CFLAGS) -Fo$* -c $*.c
	
rebuild: clean all
clean:
	del /F $(TARGET_NAME)
	del /F $(OBJ)
	del /F $(PDB_NAME)
	del /F *.pdb