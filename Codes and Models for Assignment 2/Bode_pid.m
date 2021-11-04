%%
clc
clear all
close all
G1 = tf([0.8],[1 0.8]);
G2 = tf([10],[1 10]);
G3 = tf([12],[1 12]);

w = logspace(-3,3,10000);

G_ol = G1*G2*G3;

G_cl = feedback(G_ol,[1]);

figure(1)
bode(G_ol)
grid on
% margin(G1*G2*G3)

G_p_cont = 10;
G_ol_with_P = G_p_cont*G1*G2*G3;

figure(2)
bode(G_ol_with_P,w)
grid on

G_cl_with_P = feedback(G_ol_with_P,[1]);

figure(3)
bode(G_cl_with_P,w)
grid on

G_i1_cont = tf([1],[1 0]);
G_ol_with_i1 = G_i1_cont*G1*G2*G3;

figure(4)
bode(G_ol_with_i1)
grid on

G_cl_with_i1 = feedback(G_ol_with_i1,[1]);

figure(5)
bode(G_cl_with_i1)
grid on

G_i100_cont = tf([100],[1 0]);
G_ol_with_i100 = G_i100_cont*G1*G2*G3;
G_cl_with_i100 = feedback(G_ol_with_i100,[1]);

figure(6)
bode(G_cl_with_i100)
grid on

figure(7)
bode(G_ol)
hold on
grid on
% bode(G_ol_with_P)
hold on
bode(G_ol_with_i1)
hold on
bode(G_ol_with_i100)

figure(8)
bode(G_cl)
hold on
% bode(G_cl_with_P)
hold on
grid on
bode(G_cl_with_i1)
hold on
bode(G_cl_with_i100)