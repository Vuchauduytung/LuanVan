function varargout = Engine_simulator(varargin)
% ENGINE_SIMULATOR MATLAB code for Engine_simulator.fig
%      ENGINE_SIMULATOR, by itself, creates a new ENGINE_SIMULATOR or raises the existing
%      singleton*.
%
%      H = ENGINE_SIMULATOR returns the handle to a new ENGINE_SIMULATOR or the handle to
%   handles.timerhe existing singleton*.
%
%      ENGINE_SIMULATOR('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ENGINE_SIMULATOR.M with the given input arguments.
%
%      ENGINE_SIMULATOR('Property','Value',...) creates a new ENGINE_SIMULATOR or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Engine_simulator_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Engine_simulator_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Engine_simulator

% Last Modified by GUIDE v2.5 27-Nov-2021 21:51:11

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Engine_simulator_OpeningFcn, ...
                   'gui_OutputFcn',  @Engine_simulator_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
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


% --- Executes just before Engine_simulator is made visible.
function Engine_simulator_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Engine_simulator (see VARARGIN)

% Choose default command line output for Engine_simulator
handles.output = hObject;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Engine_simulator wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Engine_simulator_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



% --- Executes on mouse press over figure background, over a disabled or
% --- inactive control, or over an axes background.
function figure1_WindowButtonUpFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if isfield(handles, "pushbutton1_value")
    pushbutton1_value = getfield(handles, "pushbutton1_value");
else
    pushbutton1_value = 0;
end
if pushbutton1_value
    handles = setfield(handles, "pushbutton1_value", 0);
    pushbutton1_MouseRelease(handles.pushbutton1, handles);
    handles.pushbutton1.Value = 0;
end


function pushbutton1_MouseRelease(hObject, handles)
hObject.BackgroundColor = [0.9400 0.9400 0.9400];
handles.timer = update_timer(hObject, handles, "ON");
guidata(hObject,handles)


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over pushbutton1.
function pushbutton1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

hObject.BackgroundColor = 'green';
handles.timer = update_timer(hObject, handles, "RUNNING");
handles.pushbutton1 = hObject;
handles = setfield(handles, "pushbutton1_value", 1);
guidata(hObject,handles)



function t = update_timer(hObject, handles, mode)
if isfield(handles, "timer")
    stop(handles.timer)
%     delete(handles.timer)
%     clear handles.timer
end
t = timer;
% handles.timer.StartFcn = @initTimer;
t.TimerFcn = {@engine_simulation, mode};
t.Period   = 0.5;
t.TasksToExecute = 10;
t.ExecutionMode  = 'fixedRate';
start(t);
guidata(hObject,handles)
return 


% --- Executes on button press in togglebutton2.
function togglebutton2_Callback(hObject, eventdata, handles)
% hObject    handle to togglebutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of togglebutton2
try
    previous_value = getfield(hObject.UserData, "previous_value");
catch
    previous_value = 0;
end
if ~previous_value
    handles.timer_enabled = 1;
    hObject.BackgroundColor = 'green';
    handles.togglebutton4.Enable = 'on';
    handles.timer = update_timer(hObject, handles, "OFF");
    hObject.UserData = setfield(hObject.UserData, 'previous_value', 1);
    set(hObject, "String", "Ngắt kết nối");
else 
    if isfield(handles, "timer")
        stop(handles.timer)
%         delete(handles.timer);
%         clear handles.timer
    end
    handles.timer_enabled = 0;
    hObject.BackgroundColor = [0.9400 0.9400 0.9400];
    handles.pushbutton1.BackgroundColor = [0.9400 0.9400 0.9400];
    handles.togglebutton4.BackgroundColor = [0.9400 0.9400 0.9400];
    handles.togglebutton4.Value = 0;
    handles.togglebutton4.String = "Đề máy";
    handles.pushbutton1.Enable = 'off';
    handles.togglebutton4.Enable = 'off';
    hObject.UserData = setfield(hObject.UserData, 'previous_value', 0);
    set(hObject, "String", "Kết nối cảm biến");    
    handles.pushbutton1.Enable = 'off';
    handles.pushbutton1.BackgroundColor = [0.9400 0.9400 0.9400];
end
% handles.togglebutton2 = hObject;
guidata(hObject,handles)



% --- Executes on button press in togglebutton4.
function togglebutton4_Callback(hObject, eventdata, handles)
% hObject    handle to togglebutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of togglebutton4

try
    previous_value = getfield(hObject.UserData, "previous_value");
catch
    previous_value = 0;
end
if ~previous_value
    handles.timer = update_timer(hObject, handles, "ON");
    hObject.BackgroundColor = 'yellow';
    handles.pushbutton1.Enable = 'inactive';
    hObject.UserData = setfield(hObject.UserData, 'previous_value', 1);
    set(hObject, "String", "Tắt máy");
else 
    handles.timer = update_timer(hObject, handles, "OFF");
    hObject.BackgroundColor = [0.9400 0.9400 0.9400];
    handles.pushbutton1.Enable = 'off';
    handles.pushbutton1.BackgroundColor = [0.9400 0.9400 0.9400];
    hObject.UserData = setfield(hObject.UserData, 'previous_value', 0);
    set(hObject, "String", "Đề máy");
end 
guidata(hObject,handles)



%% Code mô phỏng động cơ ở đây
function engine_simulation(obj, event, mode)
disp(mode);
