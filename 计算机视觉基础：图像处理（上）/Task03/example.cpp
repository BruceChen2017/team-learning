#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
	Mat src = imread("rabbit.jpg");
	if (src.empty())
	{
		cout << "无法读取图像" << endl;
		return 0;
	}
	Mat dst;

	imshow("RGB space", src);
	// RGB2GHSV
	cvtColor(src, dst, COLOR_BGR2HSV);
	imshow("Lab Space", dst);

	//RGB2GRAY
	cvtColor(src, dst, COLOR_BGR2GRAY);
	imshow("Gray Scale", dst);
	
	waitKey(0);
	return 0;
}