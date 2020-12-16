#include <iostream>
#include <string>
#include <iomanip>
#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp>

using namespace httplib;
using json = nlohmann::json;

std::string remember_webhook_way;
size_t webhooks_size;
json write_config_file;
int number = 0;
std::ofstream write_in_txt_file("log.txt");


void save_config_file(json config) {
    std::ofstream config_file("config.json");

    if (config_file.is_open()) {
        config_file << config.dump(4);
        config_file.close();
    }
    else {
        number++;
        write_in_txt_file << number << "." << u8" Не удалось открыть конфигурационный файл" << std::endl;
    }
}


std::string edit_webhook_template() {

    std::string webhooks_list = "{webhooks_list}";
    std::string Webhook_URL = "{Webhook URL}";
    std::string piece_of_HTML = u8R"(
<div class="form-row align-items-center">
    <div class="col">
        <input type="text" value="{Webhook URL}" class="form-control mb-2" disabled>
    </div>
    <div class="col">
        <button type="submit" name="del" value="{Webhook URL}" class="btn btn-danger mb-2">Удалить</button>
    </div>
</div>)";


    std::string webhooks_template;
    std::ifstream webhooks_file("Page.html");


    if (webhooks_file.is_open()) {
        getline(webhooks_file, webhooks_template, '\0');
        webhooks_file.close();
    }
    else {
        number++;
        write_in_txt_file << number << "." << u8" Не удалось открыть шаблон сайта" << std::endl;
        return "";
    }

    std::string one_piece_of_HTML;
    std::string full_piece_of_HTML;

    if (write_config_file["webhooks"].size()!=0) {
        for (int i = 0; i < write_config_file["webhooks"].size(); i++) {
            one_piece_of_HTML = piece_of_HTML;

            one_piece_of_HTML.replace(one_piece_of_HTML.find(Webhook_URL), Webhook_URL.size(), write_config_file["webhooks"][i]);
            one_piece_of_HTML.replace(one_piece_of_HTML.find(Webhook_URL), Webhook_URL.size(), write_config_file["webhooks"][i]);

            full_piece_of_HTML = full_piece_of_HTML + one_piece_of_HTML;
        }

        webhooks_template.replace(webhooks_template.find(webhooks_list), webhooks_list.size(), full_piece_of_HTML);
    }
    else {
        webhooks_template.replace(webhooks_template.find(webhooks_list), webhooks_list.size(), "");
    }
    return webhooks_template;
}

void edit_webhook_website(const Request& req, Response& res) {
    bool if_webhook_already_exist;
    if (req.has_param("set")) {

        if (req.get_param_value("set") == "") {
        }
        else {
            if_webhook_already_exist = false;
            write_config_file["webhooks"].size();

            for (int i = 0; i < write_config_file["webhooks"].size(); i++) {

                if (write_config_file["webhooks"][i] == req.get_param_value("set")) {

                    number++;
                    write_in_txt_file << number << "." << u8" Следующий вебхук уже есть: " << write_config_file["webhooks"][i] << std::endl;

                    if_webhook_already_exist = true;

                    break;
                }
            }
            if (!if_webhook_already_exist) {

                write_config_file["webhooks"].push_back(req.get_param_value("set"));

                number++;
                write_in_txt_file << number << "." << u8" Добавлен следующий вебхук:  " << req.get_param_value("set") << std::endl;

            }
        }
    }
    else if (req.has_param("del")) {

        for (int i = 0; i < write_config_file["webhooks"].size(); i++) {

            std::string remember_webhook_way = write_config_file["webhooks"][i];

            if (remember_webhook_way == req.get_param_value("del"))
            {
                write_config_file["webhooks"].erase(write_config_file["webhooks"].begin() + i);

                number++;
                write_in_txt_file << number << "." << u8" Удалён следующий вебхук: " << remember_webhook_way << std::endl;
                break;
            }
        }
    }
    save_config_file(write_config_file);
}

void webhooks_post(const Request& req, Response& res) {

    edit_webhook_website(req,res);


    res.set_content(edit_webhook_template(), "text/html; charset=UTF-8");

}

void webhooks_get(const Request& req, Response& res) {

    res.set_content(edit_webhook_template(), "text/html");

}

int main() {

    std::ifstream config_file("config.json");
    json write_config_file;

    if (config_file.is_open()) {

        config_file >> write_config_file;

    }
    else {

        write_config_file["webhooks"] = json::array();

    }

    Server svr;

    svr.Post("/webhooks", webhooks_post);
    svr.Get("/webhooks", webhooks_get);

    number++;
    write_in_txt_file << number << "." << u8" Сервер запущен" << std::endl;

    svr.listen("localhost", 1234);
}