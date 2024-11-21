#include <iostream>
#include <string>
#include "Customer.h"
#include "Operator.h"
#include "Bill.h"

using namespace std;

int main() {
    int numOperators, numCustomers;

    cout << "Enter the number of operators: ";
    cin >> numOperators;
    Operator** operators = new Operator*[numOperators]; // Динамічний масив операторів

    for (int i = 0; i < numOperators; i++) {
        int id;
        double callRate, messageCost, internetCost;
        cout << "Enter information for operator " << (i + 1) << " (ID, call rate, cost of messages, cost of Internet): ";
        cin >> id >> callRate >> messageCost >> internetCost;
        operators[i] = new Operator(id, callRate, messageCost, internetCost); // Створення нового оператора
    }

    cout << "Enter the number of customers: ";
    cin >> numCustomers;
    Customer** customers = new Customer*[numCustomers]; // Динамічний масив клієнтів

    for (int i = 0; i < numCustomers; i++) {
        int id, age, operatorId;
        string name;
        double accountLimit;
        cout << "Enter information for customer " << (i + 1) << " (ID, name, age, operator ID, account limit): ";
        cin >> id >> name >> age >> operatorId >> accountLimit;

        // Перевірка, чи оператор з ID існує
        Operator* selectedOperator = nullptr;
        for (int j = 0; j < numOperators; j++) {
            if (operators[j]->getID() == operatorId) {
                selectedOperator = operators[j];
                break;
            }
        }

        if (selectedOperator == nullptr) {
            cout << "Operator with ID " << operatorId << " not found." << endl;
            i--; // Зменшуємо i, щоб знову запросити інформацію
            continue; // Продовжити наступну ітерацію циклу
        }

        // Створення рахунку для клієнта
        Bill* bill = new Bill(accountLimit);
        customers[i] = new Customer(id, name, age, selectedOperator, bill); // Створення нового клієнта
    }

    // Ваша логіка для обробки взаємодій між клієнтами і операторами

    // Звільнення пам'яті
    for (int i = 0; i < numOperators; i++) {
        delete operators[i];
    }
    delete[] operators;

    for (int i = 0; i < numCustomers; i++) {
        delete customers[i]->getBill(); // Передбачаючи, що у вас є метод getBill()
        delete customers[i];
    }
    delete[] customers;

    return 0;
}
