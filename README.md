# Expedia App
**Expedia Travel Itinerary Management System is a comprehensive application that allows users to search and book flights and hotels for their travel needs.**

**This project is designed to enhance OOP design skills by creating a customer-focused booking system for flights, hotels, and other reservations. The system uses APIs from airlines and hotels to provide customers with available options, and integrates with payment APIs for seamless transactions.**

## Features

- **Flight Search**: Users can search for flights based on their origin, destination, departure date, return date, number of adults and children, and class preference.
- **Hotel Search**: Users can search for hotels based on their destination, check-in and check-out dates, number of adults and children, and required number of rooms.
- **Flight Reservation**: Users can reserve flights by selecting their preferred flights from the search results and providing passenger information.
- **Hotel Reservation**: Users can reserve hotels by selecting their preferred hotels from the search results and providing guest information.
- **Payment Processing**: The system supports multiple payment methods, including credit cards and PayPal, for secure and convenient payment processing.
- **Itinerary Management**: Users can view and manage their travel itineraries, including flight and hotel reservations.
- **User Management**: The system provides user authentication and user account management features, including registration, login, and profile management.

## Architecture

**The Expedia Travel Management System follows a modular architecture, consisting of several components:**

- **Backend**: Handles the core functionality of flight and hotel search, reservation, payment processing, and integration with external APIs.
- **Frontend**: Provides a user-friendly interface for customers to interact with the system and perform flight and hotel searches, reservations, and payment.
- **APIs**: Integrates with external services such as flight and hotel booking APIs, payment gateways (e.g., PayPal, Stripe), and customer information management systems (e.g., Marriott).

## APIs:
**Flights APIs:**
- Companies such as AirCanada and TurkishAirlines provide online query APIs to get current available flights
- Customers can choose from available options and either reserve or cancel their selection.

**Hotel APIs:**
- Hotels such as Hilton and Marriott provide similar APIs for customers to browse available accommodations.

**Payments:**
- expedia uses payment APIs such as Square or Stripe to process transactions seamlessly.

## Usage

1. Register a new user account or log in with an existing account.
2. Use the navigation menu to search for flights or hotels based on your travel preferences.
3. Select your desired flight or hotel from the search results and proceed to make a reservation.
4. Provide the necessary details such as passenger information, payment method, etc.
5. Confirm the reservation and complete the payment process.
6. View and manage your travel itineraries in the user dashboard.

## Contributing

**Contributions to the Expedia Travel Management System are welcome and encouraged. If you would like to contribute**

please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure that the codebase is clean and well-documented.
4. Write appropriate unit tests if applicable.
5. Commit your changes and push them to your fork.
6. Submit a pull request, describing your changes in detail and providing any relevant information or context.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AhmedHamdi0/Expedia-App.git
```

2. Navigate to the project directory:

```bash
cd Expedia-App
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Launch the application by running `Expedia-App.py`:

```bash
python Expedia-App
```

## Acknowledgements

- This project was developed as a demonstration of skills and knowledge in building a comprehensive travel management system.
- The project incorporates various concepts and techniques, including backend development, frontend design, API integration.
- The implementation was inspired by real-world travel booking platforms such as Expedia.

