#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;
int main(int argc, char* argv[])
{
	Mat img = imread("e:\\cpp_test\\rabbit.jpg");
	if (img.empty())
	{
		cout << "无法读取图像" << endl;
		return 0;
	}

	float fx, fy;
	fx = fy = 0.5;
	Mat re1, re2, re3, re4;
	// 0.5*size
	resize(img, re1, Size(), fx, fy, INTER_NEAREST);
	resize(img, re2, Size(), fx, fy, INTER_LINEAR);

	int height = img.rows;
	int width = img.cols;
	float factor = 1.5;
	Size dsize = Size(round(factor * width), round(factor * height));
	resize(img, re3, dsize, 0, 0, INTER_NEAREST);
	resize(img, re4, dsize, 0, 0, INTER_LINEAR);

	// show image
	imshow("Original image", img);
	imshow("0.5*size image by NEAREST", re1);
	imshow("0.5*size image by LINEAR", re2);
	imshow("1.5*size image by NEAREST", re3);
	imshow("1.5*size image by LINEAR", re4);
	waitKey(0);
	return 0;
}