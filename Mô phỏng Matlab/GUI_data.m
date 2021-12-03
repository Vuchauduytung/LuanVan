function varargout = GUI_data(varargin)
%GUI_DATA MATLAB code file for GUI_data.fig
%      GUI_DATA, by itself, creates a new GUI_DATA or raises the existing
%      singleton*.
%
%      H = GUI_DATA returns the handle to a new GUI_DATA or the handle to
%      the existing singleton*.
%
%      GUI_DATA('Property','Value',...) creates a new GUI_DATA using the
%      given property value pairs. Unrecognized properties are passed via
%      varargin to GUI_data_OpeningFcn.  This calling syntax produces a
%      warning when there is an existing singleton*.
%
%      GUI_DATA('CALLBACK') and GUI_DATA('CALLBACK',hObject,...) call the
%      local function named CALLBACK in GUI_DATA.M with the given input
%      arguments.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GUI_data

% Last Modified by GUIDE v2.5 27-Nov-2021 11:13:10

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GUI_data_OpeningFcn, ...
                   'gui_OutputFcn',  @GUI_data_OutputFcn, ...
                   'gui_LayoutFcn',  [], ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
   gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before GUI_data is made visible.
function GUI_data_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   unrecognized PropertyName/PropertyValue pairs from the
%            command line (see VARARGIN)

% Choose default command line output for GUI_data
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes GUI_data wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = GUI_data_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in Xylanh1.
function Xylanh1_Callback(hObject, eventdata, handles)
% hObject    handle to Xylanh1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
disp('hello')

% --- Executes on button press in Xylanh2.
function Xylanh2_Callback(hObject, eventdata, handles)
% hObject    handle to Xylanh2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in Xylanh4.
function Xylanh4_Callback(hObject, eventdata, handles)
% hObject    handle to Xylanh4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in Xylanh3.
function Xylanh3_Callback(hObject, eventdata, handles)
% hObject    handle to Xylanh3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in Khoidong.
function Khoidong_Callback(hObject, eventdata, handles)
% hObject    handle to Khoidong (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
getxylanh1 = get(handles.Xylanh1,'value');
if getxylanh1 == 1
    set(handles.edit)
end

% Hint: get(hObject,'Value') returns toggle state of Khoidong


% --- Executes during object creation, after setting all properties.
function uibuttongroup2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to uibuttongroup2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called



function edit_Callback(hObject, eventdata, handles)
% hObject    handle to edit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit as text
%        str2double(get(hObject,'String')) returns contents of edit as a double


% --- Executes during object creation, after setting all properties.
function edit_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
