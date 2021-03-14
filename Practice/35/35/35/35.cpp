#include<iostream>

using namespace std;

struct IntArray {
	int* data;
	int size;
};

void create(IntArray* arr, int size) {
	arr->data = new int[size];
	arr->size = size;
};


void create(IntArray& arr, int size) {
	/*arr.data = new int[size];
	arr.size = size;
	for (int i = 0;i < size;i++) {
		arr.data[i] = i;
	}*/
	create(&arr, size);
};

int get(IntArray* arr, int index) {
	if (index >= arr->size || index < 0) {
		cout << "Error";
		exit(0);
	}
	return arr->data[index];
};


int get(IntArray& arr, int index) {
	/*if (index > arr.size || index < 0) {
		cout << "Error";
		exit(0);
	}
	return arr.data[index];*/
	get(&arr, index);
	return arr.data[index];
};

void set(IntArray* arr, int index, int value) {
	if (index > arr->size || index < 0) {
		cout << "error";
		exit(0);
	}
	arr->data[index] = value;
};

void set(IntArray& arr, int index, int value) {
	/*if (index > arr.data.size() || index < 0) {
		cout << "Error";
		exit(0);
	}
	arr.data[index] = value;*/
	set(&arr, index, value);
};

void print(IntArray* arr) {
	cout << '[';
	for (int i = 0; i < arr->size;i++) {
		if (i == arr->size - 1) {
			cout << arr->data[i]<<']'<<endl;
			break;
		}
		cout << arr->data[i] << " ";
	}

};
void print(IntArray& arr) {
	/*for (int i = 0; i < arr.data.size();i++) {
		cout << arr.data[i] << " ";
	}*/
	print(&arr);
};

void resize(IntArray* arr, int newSize) {
	if (newSize > arr->size) {
		int* newMas = new int[newSize];
		memcpy(newMas, arr->data, sizeof(int) * arr->size); 
		for (int i = arr->size; i < newSize; ++i)
			newMas[i] = 0;
		delete[] arr->data;
		arr->data = newMas;
		arr->size = newSize;

	}
	else if (newSize < arr->size) {
		int* newMas = new int[newSize];
		for (int i = 0; i < newSize;i++)
			newMas[i] = arr->data[i];
		delete[] arr->data;
		arr->data = newMas;
		arr->size = newSize;
	}
};


void resize(IntArray& arr, int newSize) {
	resize(&arr, newSize);
};




void destroy(IntArray* arr) {
	if (!arr->data) {
		return;
	}
	delete[] arr->data;
	arr->data = nullptr;
	arr->size = 0;
};

void destroy(IntArray& arr) {
	destroy(&arr);
};



int main() {
	IntArray mas;

	//create(&arr, size);
	create(mas, 30);

	for (int i = 0; i < 30; i++) {
		set(mas, i, i + 1);
	}

	//get(&arr,index);
	print(mas);
	
	//set(&arr,index,value);
	resize(mas, 50);

	//print(&arr);
	print(mas);

	//resize(&arr,newSize);
	resize(mas, 10);
	print(mas);

	//destroy(&arr);
	destroy(mas);
}