# ecom-ms

## Assessment Document for Backend Microservices Development

## Overview

The goal of this assessment is to evaluate your ability to develop a backend system using a microservices architecture. You are required to create a system with three services, communicate asynchronously using RabbitMQ, use MySQL for the database, write unit tests, and set up a CI/CD pipeline with Jenkins and Docker.

## Requirements

### Microservices Architecture

- Develop three microservices:
  - **Customer Service** (Python)
  - **Order and Product Service** (Java | Spring Boot)
  - **Notification Service** (Python)
- All services should use MySQL as the database.

### Asynchronous Communication

- Use RabbitMQ to enable asynchronous communication between the services.
- Specifically, use asynchronous communication to simulate a notification after making a purchase.

### Unit Testing

- Write unit tests for all services to ensure code quality and correctness.
- Include a brief research report on different types of tests.

### CI/CD Pipeline

- Implement a CI/CD pipeline using Jenkins that includes the phases: Build, Test, and Deploy.
- Use Docker to containerize the services.

## Instructions

### Customer Service (Python)

#### Setup

- Create a Flask or Django application for Customer Service.
- Integrate MySQL for data storage.

#### Functional Requirements

- Implement CRUD operations for managing Customer entities.

**Schema for Customer**

```json
{
  "id": "integer",
  "firstname": "string",
  "lastname": "string",
  "email": "string",
  "phoneNumber": "string"
}
```


 ### Order and Product Service (Java)

#### Setup:
- Create a Spring Boot application for the Order and Product Service.
- Integrate MySQL (or H2 ) for data storage.

#### Functional Requirements:

- Implement CRUD operations for managing Product and Order entities.
  
**Schema for Product**
```json
{
  "id": "integer",
  "productName": "string",
  "unitPrice": "double",
  "quantity": "integer"
}
```


**Schema for Order**
```json
{
  "id": "integer",
  "userId": "integer",
  "orderItems": [
    {
      "productId": "integer",
      "quantity": "integer",
      "totalPrice": "double"
    }
  ],
  "totalAmount": "double",
  "paymentMethod": "string"
}
```

### Notification Service (Python)

##### Setup

- Create a Flask or Django application for the Notification Service.
- Integrate RabbitMQ

#### Functional Requirements

- Consume messages from RabbitMQ sent by the Order and Product Service.
- Simulate sending a notification when a purchase is made.

### Asynchronous Communication

#### Use RabbitMQ to enable communication between the services:

- The Order and Product Service should publish a message to RabbitMQ when an order is created.
- The Notification Service should consume the message and simulate sending a notification.

### Unit Testing

- Write unit tests for all services to cover the CRUD operations.
- Use appropriate testing frameworks: unittest or pytest for Python and JUnit for Java.

### CI/CD Pipeline

Use Jenkins to automate the pipeline with the following stages:

1. **Build**: Compile the code and build the Docker images.
2. **Test**: Run unit tests.
3. **Deploy**: Deploy the Docker containers to a environment.

### Documentation

The project should include comprehensive documentation with:

1. Overview:

    - Description of the project.
    - Technologies used.

2. Setup Instructions:

    - How to set up the development environment.
    - How to run the services locally.

3. API Documentation:

    - Detailed documentation of the API endpoints. (OpenAPI | Swagger)

4. CI/CD Pipeline:

    - Explanation of the Jenkins pipeline setup.
    - How to trigger builds and deployments.

5. Testing:

    - Explanation of the unit tests.
    - Brief research report on different types of tests.

### Submission

Submit your completed project in a Git repository. The repository should include:

1. Source code for all services.
2. Dockerfile for each service.
3. Configuration files for RabbitMQ and MySQL.
4. Unit tests for all services.
5. Jenkins pipeline configuration.
6. Comprehensive documentation.

### Evaluation Criteria

1. Correctness and functionality of the microservices.
2. Proper use of RabbitMQ for asynchronous communication.
3. Quality and coverage of unit tests.
4. Proper implementation of the CI/CD pipeline using Jenkins.
5. Adherence to best practices in coding and project structure.
6. Quality and clarity of the documentation.


# Good luck!

