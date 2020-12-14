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

    const std::string webhooks_list = "{webhooks_list}";
    const std::string Webhook_URL = "{Webhook URL}";
    const std::string piece_of_HTML = u8R"(
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


    std::string full_piece_of_HTML;
    webhooks_size = write_config_file["webhooks"].size();

    if (webhooks_size) {
        for (int i = 0; i < webhooks_size; i++) {
            remember_webhook_way = write_config_file["webhooks"][i];
            std::string one_piece_of_HTML = piece_of_HTML;

            one_piece_of_HTML.replace(one_piece_of_HTML.find(Webhook_URL), Webhook_URL.size(), remember_webhook_way);
            one_piece_of_HTML.replace(one_piece_of_HTML.find(Webhook_URL), Webhook_URL.size(), remember_webhook_way);

            full_piece_of_HTML = full_piece_of_HTML + one_piece_of_HTML;
        }

        webhooks_template.replace(webhooks_template.find(webhooks_list), webhooks_list.size(), full_piece_of_HTML);
    }
    else {
        webhooks_template.replace(webhooks_template.find(webhooks_list), webhooks_list.size(), "");
    }
    return webhooks_template;
}

void edit_webhook_website(const Request& req) {
    if (req.has_param("set")) {
        std::string set_webhook = req.get_param_value("set");

        if (set_webhook == "") {
        }
        else {

            webhooks_size = write_config_file["webhooks"].size();
            bool if_webhook_already_exist = false;

            for (int i = 0; i < webhooks_size; i++) {
                remember_webhook_way = write_config_file["webhooks"][i];

                if (remember_webhook_way == set_webhook) {

                    number++;
                    write_in_txt_file << number << "." << u8" Следующий вебхук уже есть: " << remember_webhook_way << std::endl;

                    if_webhook_already_exist = true;

                    break;
                }
            }
            if (!if_webhook_already_exist) {

                write_config_file["webhooks"].push_back(set_webhook);

                number++;
                write_in_txt_file << number << "." << u8" Добавлен следующий вебхук:  " << set_webhook << std::endl;

            }
        }
    }
    else if (req.has_param("del")) {

        std::string del_webhook = req.get_param_value("del");
        webhooks_size = write_config_file["webhooks"].size();

        for (int i = 0; i < webhooks_size; i++) {

            std::string remember_webhook_way = write_config_file["webhooks"][i];

            if (remember_webhook_way == del_webhook)
            {
                write_config_file["webhooks"].erase(write_config_file["webhooks"].begin() + i);

                number++;
                write_in_txt_file << number << "." << u8" Удалён следующий вебхук: " << remember_webhook_way << std::endl;

            }
        }
    }
    save_config_file(write_config_file);
}

void webhooks_post(const Request& req, Response& res) {

    edit_webhook_website(req);

    std::string send_response = edit_webhook_template();

    res.set_content(send_response, "text/html; charset=UTF-8");

}

void webhooks_get(const Request& req, Response& res) {

    std::string send_response = edit_webhook_template();

    res.set_content(send_response, "text/html");

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