clear
clc
close all

%% Initialization

% read json file
struct_json = json_parse('mocap_config.json');

% These two are IP address and port for receiving data.
IP_recv = struct_json.HOST_UDP;
Port_recv = str2double(struct_json.PORT_UDP);

% These two are IP address and port for sending data.
% Here, we don't send data.
% IP_send = IP_recv;
% Port_send = str2double(struct_json.PORT_UDP_SEND_AGAIN);

% This line creates a UDP object to send and receive data.
% udp_obj = udp(IP_send, Port_send, ...
%     'LocalHost', IP_recv, 'LocalPort', Port_recv);

udp_obj = udp('', ...
    'LocalHost', IP_recv, 'LocalPort', Port_recv);

% number of bytes for receiving message
udp_obj.InputBufferSize = str2double(struct_json.DATA_BYTES_LENGTH_UDP);

% number of bytes for send message
% Here, we don't send data.
% udp_obj.OutputBufferSize = str2double(struct_json.DATA_BYTES_LENGTH_UDP);

% Be aware that there are little endian and big endian.
% The endian may change across platforms.
udp_obj.ByteOrder = 'littleEndian';

% open ports
fopen(udp_obj);
disp("open")
fclose(udp_obj);

% dimension of received data, here is a vector
sizeA = str2double(struct_json.DATA_BYTES_LENGTH_UDP)/8;

%% Receive data
while true
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Receive data
    % open to read
    fopen(udp_obj);
    packetData = fread(udp_obj, sizeA, 'double');
    disp("Received data");
    disp(packetData);
    % remember to close
    fclose(udp_obj);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    
    %%%%%%%%%%%%%%%%%%%%%
    % Send data
    % open to send
%     fopen(udp_obj);
%     fwrite(udp_obj, packetData, 'double') ;
%     disp("Sent data");
%     % remember to close
%     fclose(udp_obj);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    
    pause(1.0)
end