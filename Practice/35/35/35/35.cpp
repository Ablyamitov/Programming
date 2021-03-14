#include<iostream>
#include<cstring>
using namespace std;

struct IntArray {
	int* data;
	int size;
};

void create(IntArray* arr, int size) {
	arr->data = new int[size];
	arr->size = size;
	for (int i = 0;i < size;i++) {
		arr->data[i] = i;
	}
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
	for (int i = 0; i < arr->size;i++) {
		cout << arr->data[i]<<" ";
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
			arr->data[i] = 0;
		delete[] arr->data;
		arr->data = newMas;
		arr->size = newSize;

	}
	else if (newSize < arr->size) {
		int* newMas = new int[newSize];
		for(int i = 0; i<newSize;i++)
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
	delete[] arr->data;
	arr->data = nullptr;
	arr->size = 0;
};

void destroy(IntArray& arr) {
	destroy(&arr);
};



int main() {
	IntArray mas;
	setlocale(LC_ALL, "Rus");
	int size = 30;
	int index, value, newSize;
	cout << "Введите номер элемента, значение элемента и новый размер массива: "<<endl;
	cin >> index >> value >> newSize;

	//create(&arr, size);
	create(mas, size);

	//get(&arr,index);
	get(mas, index);
	cout <<endl<< "Первоначальный массив без изменения: " << endl;
	print(mas);

	//set(&arr,index,value);
	set(mas, index, value);
	cout << endl << "Массив после изменения элемента: "<<endl;
	//print(&arr);
	print(mas);

	//resize(&arr,newSize);
	resize(mas, newSize);
	cout << endl << "Массив после изменения размера: " << endl;
	print(mas);

	//destroy(&arr);
	destroy(mas);
}