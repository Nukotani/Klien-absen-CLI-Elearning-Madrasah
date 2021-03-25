.PHONY: clean
FILE_TO_LINK = socket.o parsers.o error.o
absen: socket.o parsers.o error.o
	cc src/main.c $(FILE_TO_LINK) -o $@
socket.o:
	cc -c src/socket.c -o $@
parsers.o:
	cc -c src/parsers.c -o $@
error.o:
	cc -c src/error.c -o $@
clean:
	rm $(FILE_TO_LINK)	
