# Skylog API Routemap

## Top level

### `/` - GET
- **Description**: Heartbeat endpoint to check if the server is running, get version info, server time, uptime, and other details.

## Authentication

Main authentication is handled via Firebase Authentication.

## Search

## Users

These are the endpoints for user related operations and queries.

### `/api/v1/users/profile/[user_id]` - GET
- **Description**: Get public facing profile information for a user.
- **URL Parameters**:
  - `user_id` (string): The ID of the user whose profile is being requested.
- **Query Parameters**: None
- **Request Body**:
  - 
- **Response**: A JSON object representing the user's profile.

#### Example Request:
```http
GET /api/v1/users/profile/12345
```

#### Example OK response:
```json
{}
```

#### Example Error response (404):
```json
{
  "error": "User not found"
}
```

### `/api/v1/users/create` - POST
- **Description**: Create a new user account.


## Aircraft

## Airports

## Flight Plans

## Facilities

## Weather

## Notifications

## Rentals
