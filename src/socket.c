#include "socket.h"
#include "parsers.h"

int makesocket() {
	int sockfd; 
	struct sockaddr_in server_address;
	
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0)
		error("gagal membuka socket");

	server_address.sin_family = AF_INET;
	server_address.sin_port = (unsigned short)20480;
	server_address.sin_addr.s_addr = (unsigned long) 179114286;
	
	if (connect(sockfd, (struct sockaddr *) &server_address, sizeof(server_address)) < 0)
		error("gagal menyambungkan");
	return sockfd;
}
void client_connect(int sockfd, char uri[], char cookie[], bool post_flag, char buffer[]) {
	int n;
	char post_data[255], post_data_length[3];

	if (post_flag) {
		strcpy(buffer, "POST ");
	}
	else {
		strcpy(buffer, "GET ");
	}

	strcat(buffer, uri);
	strcat(buffer, " HTTP/1.1\r\nHost: elearning.man1balam.sch.id\r\nUser-Agent: Trust Me Im Mozilla\r\nAccept: */*\r\n");

	if (!post_flag) {
		strcat(buffer, "Cookie: ");
		strcat(buffer, cookie);
		strcat(buffer, "\r\n");
	}
	else {
		account_parser(post_data);
		strcat(buffer, "Content-Length: ");
		sprintf(post_data_length, "%d", strlen(post_data));
		strcat(buffer, post_data_length);
		strcat(buffer, "\r\n");
		strcat(buffer, "Content-Type: application/x-www-form-urlencoded\r\n");
	}

	strcat(buffer, "\r\n");
	if (post_flag)
		strcat(buffer, post_data);
	n = write(sockfd, buffer, strlen(buffer));
	if (n < 0)
		error("gagal menulis ke socket");

	memset(buffer, 0, strlen(buffer));

	n = read(sockfd, buffer, 500);
	if (n < 0)
		error("gagal membaca socket");

	buffer[strlen(buffer)] = '\0';
}
