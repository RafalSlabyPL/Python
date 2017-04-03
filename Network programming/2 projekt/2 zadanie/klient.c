#include "connectsock.c"
#define UNIXEPOCH 2208988800ul
int main(int argc, char **argv){
 int s;
 char msg[] = "ktora godzina?";
 time_t now;
 if ((s = connectsock(argv[1], "time", "udp"))<0) return 0;
 write(s, msg, strlen(msg));
 if (read(s, (char *)&now, sizeof(now))<0) return 0;
 else{
 now = ntohl((u_long)now);
 now -= UNIXEPOCH;
 printf("%s\n", ctime(&now));
 }
 if (shutdown(s, SHUT_RDWR)<0) return 0;
 return 1;
}
