[y,fs]=audioread("SYB35.wav")
ts=1/fs;
t=(0:length(y)-1)*ts;
k=(0:length(y)-1)*fs/length(y);

x=fft(y);
subplot(3,1,1);
plot(k,abs(x));
title("fft of original signal")
xlabel("frequency");
ylabel("amplitude");
[y1,fs1]=audioread("noisy35.wav");

ts1=1/fs1;
t1=(0:length(y1)-1)*ts1;
k1=(0:length(y1)-1)*fs1/length(y1);

x1=fft(y1);
subplot(3,1,2);
plot(k1,abs(x1));
title("fft of noisy signal")
xlabel("frequency");
ylabel("amplitude");
%sound(y1,fs1);


y2 = filter(test,1,x3);   %1795-10000
%x2=fft(y2);
%subplot(3,1,3);
%plot(k,abs(x2));
%sound(y2,fs)

y3=filter(test1,1,y2)     %11010-22049
x3=fft(y3);

subplot(3,1,3);
plot(k,abs(x3));
title("fft of filtered signal")
xlabel("frequency");
ylabel("amplitude");
sound(y3,fs);




