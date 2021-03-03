#include "socket.h"
#include "error.h"
#include "parsers.h"
#include "schedule.h"

int main(){
	int sockfd = makesocket();
	char *response = client_connect(sockfd, "/login/do_login", "d", 1);
	login_check(response);
	char *cookie = cookie_parser(response);
	free(response);
	close(sockfd);
	size_t *schedule_size;
	schedule *schedule_array = schedule_parser(schedule_size); 
	for (size_t i = 0; i < *schedule_size; i++) {
		sockfd = makesocket();
		printf("Mengisi absen %s\n", schedule_array[i].name);
		response = client_connect(sockfd, schedule_array[i].link, cookie, 0);
		printf("berhasil\n");
		free(response);
		close(sockfd);
	}
	close(sockfd);
	return 0;
}
