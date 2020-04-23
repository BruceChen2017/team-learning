#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
	Mat img = imread("rabbit.jpg");
	if (img.empty())
	{
		cout << "无法读取图像" << endl;
		return 0;
	}

	// rotation
	Point center = Point(img.cols / 2, img.rows / 2);
	double angle = -90.0;
	double scale = 1.0;
	Mat rot_matrix = getRotationMatrix2D(center, angle, scale);
	// https://stackoverflow.com/questions/7970988/print-out-the-values-of-a-mat-matrix-in-opencv-c
	cout << "rot_matrix = " << endl << " "  << rot_matrix << endl << endl;
	Mat rot_dst;
	warpAffine(img, rot_dst, rot_matrix, img.size());

	// translation
	Mat trans_matrix = Mat::zeros(2, 3, CV_32FC1);
	trans_matrix.at<float>(0, 0) = 1;
	trans_matrix.at<float>(0, 2) = 10; // 水平
	trans_matrix.at<float>(1, 1) = 1;
	trans_matrix.at<float>(1, 2) = 20; // 垂直
	cout << "trans_matrix = " << endl << " " << trans_matrix << endl << endl;
	// get inverse affine matrix for test
	Mat itrans_matrix;
	invertAffineTransform(trans_matrix, itrans_matrix);
	// should be inverse of trans_matrix
	//			[,1] [,2] [,3]
	//	[1, ]    1    0   10
	//	[2, ]    0    1   20  
	//	[3, ]    0    0    1
	//             ||
	//			[,1] [,2] [,3]
	//	[1, ]    1    0   -10
	//	[2, ]    0    1   -20
	//	[3, ]    0    0     1
	cout << "inverse_trans_matrix = " << endl << " " << itrans_matrix << endl << endl;

	Mat trans_dst;
	warpAffine(img, trans_dst, trans_matrix, img.size());

	// show image
	imshow("Original image", img);
	imshow("Rotated image", rot_dst);
	imshow("Translated image", trans_dst);
	waitKey(0);
	return 0;
}
