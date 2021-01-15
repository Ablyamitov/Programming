#include<iostream>

#include<vector>

#include<ctime>

#include <cstdlib>

#include<string>

using namespace std;



struct Coin
{
	unsigned int count;
};
enum Element {
	FIRE,
	WATER,
	EARTH,
	AIR
};

struct Rune
{
	short level;
	Element element;
};

struct Weapon
{
	unsigned int damage;
	short critical;
	short durability;
};

struct Armor
{
	unsigned int guard;
	short durability;
};
enum ItemType
{
	COIN,
	RUNE,
	WEAPON,
	ARMOR
};

struct Item
{
	ItemType character;

	union
	{
		Coin coin;
		Rune rune;
		Weapon weapon;
		Armor armor;
	}gift;

};

const vector<double> probability{ 50.0, 6.0, 13.0, 7.0, 14.0, 0.6, 1.3, 0.4, 1.7, 0.06, 0.13, 0.07, 0.14, 1.4, 1.4, 2.8 };
Item prize(int score)
{
	if (score == 1)
		return Item{ COIN,{.coin = { 1000 }} };
	else if (score == 2)
		return  Item{ RUNE,{.rune = {1, FIRE}} };
	else if (score == 3)
		return  Item{ RUNE,{.rune = {1, WATER}} };
	else if (score == 4)
		return Item{ RUNE,{.rune = {1, EARTH}} };
	else if (score == 5)
		return  Item{ RUNE,{.rune = {1, AIR}} };
	else if (score == 6)
		return  Item{ RUNE,{.rune = {5, FIRE} } };
	else if (score == 7)
		return  Item{ RUNE,{.rune = {5, WATER} } };
	else if (score == 8)
		return  Item{ RUNE,{.rune = {5, EARTH} } };
	else if (score == 9)
		return  Item{ RUNE,{.rune = {5, AIR}} };
	else if (score == 10)
		return  Item{ RUNE,{.rune = {10, FIRE}} };
	else if (score == 11)
		return  Item{ RUNE,{.rune = {10, WATER} } };
	else if (score == 12)
		return  Item{ RUNE,{.rune = {10, EARTH}} };
	else if (score == 13)
		return  Item{ RUNE,{.rune = {10, AIR}} };
	else if (score == 14)
		return  Item{ WEAPON,{.weapon = {100, 0, 100}} };
	else if (score == 15)
		return  Item{ WEAPON,{.weapon = {75, 50, 100} } };
	else if (score == 16)
		return  Item{ ARMOR,{.armor = {50,100}} };
}
using LootBox = vector<Item>;

std::ostream& operator << (std::ostream& out, Item item) {
	if (item.character == ItemType::COIN) {
		out << "1000 gold";
	}
	else if (item.character == ItemType::RUNE) {
		short int_lvl = item.gift.rune.level;
		string string_lvl = to_string(int_lvl);
		out << "Rune of ";
		if (item.gift.rune.element == FIRE)
			out << "fire " << string_lvl << " lvl";
		else if (item.gift.rune.element == WATER)
			out << "water " << string_lvl << " lvl";
		else if (item.gift.rune.element == EARTH)
			out << "earth " << string_lvl << " lvl";
		else if (item.gift.rune.element == AIR)
			out << "air " << string_lvl << " lvl";
	}
	else if (item.character == ItemType::WEAPON) {
		if (item.gift.weapon.critical == 0)
			out << "God Killer";
		else if (item.gift.weapon.critical == 50)
			out << "Demon Slayer";
	}
	else if (item.character == ItemType::ARMOR)
		out << "Bronezhiletka";
	return out;
}
std::ostream& operator << (std::ostream& out, LootBox lootbox)
{
	return out << lootbox[0] << endl << lootbox[1] << endl << lootbox[2] << endl;
}

LootBox generateLootBox()
{
	srand(time(0));
	LootBox lootbox;
	double random_probability;

	for (int i = 0; i < 3; ++i)
	{
		random_probability = (rand() % 10001) / 100;
		int score = 0;

		double counter = 0;
		for (int i = 0;i < probability.size();i++)
		{
			++score;
			if (counter <= random_probability and random_probability < counter + probability[i])
			{
				Item random_item = prize(score);
				lootbox.push_back(random_item);
				break;
			}

			counter += probability[i];
		}
	}

	return lootbox;
}


int main()
{
	setlocale(LC_ALL, "RUS");
	bool if_yes = true;
	string response;
	while (if_yes)
	{
		cout << "Открыть лутбокс? Yes/No" << endl;
		cin >> response;

		if ((response == "y") || (response == "yes") || (response == "Y") || (response == "Yes")) {
			cout << endl;
			cout << generateLootBox();
			cout << endl;
			if_yes = true;
		}
		else if ((response == "n") || (response == "no") || (response == "N") || (response == "No")) {
			if_yes = false;
			continue;
		}
		else {
			cout << endl;
			if_yes = true;
			cout << endl;
			continue;
		}
	}
}


