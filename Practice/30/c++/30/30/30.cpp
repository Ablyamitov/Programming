#include<iostream>

#include<vector>

#include<ctime>
#include <cstdlib>

#include<string>

using namespace std;

struct Item
{
	enum class ItemType
	{
		COIN,
		RUNE,
		WEAPON,
		ARMOR
	}character;

	union 
	{
		Coin coin;
		Rune rune;
		Weapon weapon;
		Armor armor;
	}gift;

};


struct Coin 
{
	unsigned int count;
};

struct Rune 
{
	short level;
	enum class Element 
	{
		FIRE,
		WATER,
		EARTH,
		AIR
	}element;
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

const vector<double> probability{50.0, 6.0, 13.0, 7.0, 14.0, 0.6, 1.3, 0.4, 1.7, 0.06, 0.13, 0.07, 0.14, 1.4, 1.4, 2.8};
Item prize(short num)
{
	if (num == 1)
		return Item{Item::ItemType::COIN,{.coin = Coin{ 1000 }}};
	else if (num == 2)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune{1, FIRE}} };
	else if (num == 3)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune{1, WATER}} };
	else if (num == 4)
		return Item{ Item::ItemType::RUNE,{.rune = Rune{1, EARTH}} };
	else if (num == 5)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {1, AIR}} };
	else if (num == 6)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune{5, FIRE} }};
	else if (num == 7)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {5, WATER} }};
	else if (num == 8)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {5, EARTH} } };
	else if (num == 9)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {5, AIR}}} ;
	else if (num == 10)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {10, FIRE}} };
	else if (num == 11)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {10, WATER} } };
	else if (num == 12)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune{10, EARTH}} };
	else if (num == 13)
		return  Item{ Item::ItemType::RUNE,{.rune = Rune {10, AIR}}  };
	else if (num == 14)
		return  Item{ Item::ItemType::WEAPON,{.weapon = Weapon {100, 0, 100}} };
	else if (num == 15)
		return  Item{ Item::ItemType::WEAPON, {.weapon = Weapon{75, 50, 100} } };
	else if (num == 16)
		return  Item{ Item::ItemType::ARMOR,{.armor = Armor{50,100}} };
}


std::ostream& operator << (std::ostream& out, Item item){
	if (item.character == Item::ItemType::COIN) {
		out << "1000 gold";
	}
	else if (item.character == Item::ItemType::RUNE) {
		short int_lvl = item.gift.rune.level;
		string string_lvl = to_string(int_lvl);
		out << "Rune of ";
		if (item.gift.rune.element == Rune::Element::FIRE)
			out << "fire " << string_lvl << " lvl";
		else if (item.gift.rune.element == Rune::Element::WATER)
			out << "water " << string_lvl << " lvl";
		else if (item.gift.rune.element == Rune::Element::EARTH)
			out << "earth " << string_lvl << " lvl";
		else if (item.gift.rune.element == Rune::Element::AIR)
			out << "air " << string_lvl << " lvl";
	}
	else if (item.character == Item::ItemType::WEAPON) {
		if (item.gift.weapon.critical == 0)
			out << "God Killer";
		else if (item.gift.weapon.critical == 50)
			out << "Demon Slayer";
	}
	else if (item.character == Item::ItemType::ARMOR)
		out << "Bronezhiletka";
	return out;
}
std::ostream& operator << (std::ostream& out, LootBox lootbox)
{
	return out << lootbox[0] << endl << lootbox[1] << endl << lootbox[2] << endl;
}

using LootBox = vector<Item>;
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
		for (int i = 0;i<probability.size();i++)
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
			cout << generateLootBox();
			if_yes = true;
		}
		else if ((response == "n") || (response == "no") || (response == "N") || (response == "No")) {
			if_yes = false;
			continue;
		}
		else{
			if_yes = true;
			continue;
		}
	}
}


