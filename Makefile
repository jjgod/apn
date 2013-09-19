CC = clang
CFLAGS = -Wall

apn: AssignPhoneticName.o
	clang -Wall -framework Foundation -framework CoreFoundation -framework AddressBook $< -o $@