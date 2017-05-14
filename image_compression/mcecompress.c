#include ,stdlib.h
#include <prune-image.h>
#include <mce.h>

int main(int argc, char *argv[]) {
	Image *img;

	pm_init(argv[0],0);
	img = read_image("imagename.ppg");
	
}