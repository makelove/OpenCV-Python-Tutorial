#include<iostream>
#include<cstdlib>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;
Mat kernel = Mat::ones(15, 15, CV_8UC1);
class Morph{
private:
	int dilationElem,erodeElem;
	int dilationSize,erodeSize;
	
public:
	Morph(){
		dilationElem=0;
		erodeElem=0;
		dilationSize=2;
		erodeSize=2;
	}
	Mat dilateImage(Mat input){
		Mat temp,element;
		int dilationType;
		if(dilationElem==0)
			dilationType=MORPH_RECT;
		else if(dilationElem==1)
			dilationType=MORPH_CROSS;
		else if(dilationElem==2)
			dilationType=MORPH_ELLIPSE;
		element= getStructuringElement(dilationType,Size(2*dilationSize+1,2*dilationSize+1),Point(dilationSize,dilationSize));
		dilate(input,temp,kernel);
		return temp;
	}
	Mat erodeImage(Mat input){
		Mat temp,element;
		int erodeType;
		if(erodeElem==0)
			erodeType=MORPH_RECT;
		else if(erodeElem==1)
			erodeType=MORPH_CROSS;
		else if(erodeElem==2)
			erodeType=MORPH_ELLIPSE;
		element= getStructuringElement(erodeType,Size(2*erodeSize+1,2*erodeSize+1),Point(erodeSize,erodeSize));
		dilate(input,temp,kernel);
		return temp;
	}
};
int main(int argc, char **argv){
	if(argc!=2){
		cout<<"Wait for an image"<<endl;
		return -1;
	}
	vector<vector<Point> > contours;
	Mat inputMaze,gray,binary,dilation,erosion,imgDiff,BGRcomp[3],imgDiff_inv,output,red,green;
	Morph mp;
	inputMaze=imread(argv[1],CV_LOAD_IMAGE_COLOR);
	cvtColor(inputMaze,gray,CV_BGR2GRAY);
	threshold(gray,binary,127,255,CV_THRESH_BINARY_INV);

	findContours(binary,contours,CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);
	drawContours(binary, contours, 0, CV_RGB(255,255,255), CV_FILLED);
	threshold(binary,binary,240,255,CV_THRESH_BINARY);

	dilation=mp.dilateImage(binary);
	erosion=mp.erodeImage(dilation);
	absdiff(dilation,erosion,imgDiff);
	bitwise_not(imgDiff,imgDiff_inv);
	split(inputMaze,BGRcomp);
	namedWindow("diff",WINDOW_AUTOSIZE);
	imshow("diff",imgDiff);
	bitwise_and(BGRcomp[2],BGRcomp[2],red,imgDiff_inv);
	bitwise_and(BGRcomp[1],BGRcomp[1],green,imgDiff_inv);
	BGRcomp[2]=red.clone();
	BGRcomp[1]=green.clone();
	merge(BGRcomp,3,output);
	namedWindow("SolvedMaze",WINDOW_AUTOSIZE);
	imshow("SolvedMaze",output);
	//imwrite("OutputMaze.jpg",output);
	waitKey(0);
	return 0;
}