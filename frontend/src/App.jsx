import { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [userId, setUserId] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/users");

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to load users");
      }

      setUsers(data);
    } catch (error) {
      setMessage(error.message);
    }
  };

  const createOrder = async () => {
    try {
      if (!userId) {
        setMessage("Please select a user");
        return;
      }

      if (!description.trim()) {
        setMessage("Please enter an order description");
        return;
      }

      const response = await fetch("http://127.0.0.1:8000/orders", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: Number(userId),
          description: description,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to create order");
      }

      setMessage(`Order created: ${data.order_id}`);
      setDescription("");
    } catch (error) {
      setMessage(error.message);
    }
  };

  return (
    <div>
      <h1>AI Order Processing Platform</h1>

      <h2>Create Order</h2>

      <label>User</label>

      <select
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      >
        <option value="">Select a user</option>

      {users.map((user) => (
        <option key={user.user_id} value={user.user_id}>
          {user.username}
        </option>
      ))}
      </select>

      <br />
      <br />

      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Enter order description..."
      />

      <br />

      <button onClick={createOrder}>
        Create Order
      </button>

      <p>{message}</p>
    </div>
  );
}

export default App;