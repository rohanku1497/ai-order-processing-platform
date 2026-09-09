import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);
  const [userId, setUserId] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");
  const [orders, setOrders] = useState([]);
  const [processedOrder, setProcessedOrder] = useState(null);
  const [processingOrderId, setProcessingOrderId] = useState(null);

  // Load users and orders when page opens
  useEffect(() => {
    loadUsers();
    loadOrders();
  }, []);

  // GET /users
  const loadUsers = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/users"
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to load users"
        );
      }

      setUsers(data);
    } catch (error) {
      setMessage(error.message);
    }
  };

  // GET /orders
  const loadOrders = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/orders"
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to load orders"
        );
      }

      setOrders(data);
    } catch (error) {
      setMessage(error.message);
    }
  };

  // POST /orders
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

      const response = await fetch(
        "http://127.0.0.1:8000/orders",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            user_id: Number(userId),
            description: description,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to create order"
        );
      }

      setMessage(`Order created: ${data.order_id}`);
      setDescription("");

      await loadOrders();
    } catch (error) {
      setMessage(error.message);
    }
  };

  // POST /orders/{order_id}/process
  const processOrder = async (orderId) => {
    try {
      setProcessingOrderId(orderId);
      setMessage("");

      const response = await fetch(
        `http://127.0.0.1:8000/orders/${orderId}/process`,
        {
          method: "POST",
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to process order"
        );
      }

      setMessage(
        `Order ${orderId} processed successfully`
      );

      await loadOrders();
    } catch (error) {
      setMessage(error.message);
    } finally {
      setProcessingOrderId(null);
    }
  };

  // GET /orders/{order_id}/processed
  const getProcessedOrder = async (orderId) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/orders/${orderId}/processed`
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to get processed order"
        );
      }

      setProcessedOrder(data);
      setMessage("");
    } catch (error) {
      setMessage(error.message);
    }
  };

  return (
    <div className="container">
      <h1>AI Order Processing Platform</h1>

      {/* CREATE ORDER */}
      <div className="card">
        <h2>Create Order</h2>

        <label>User</label>

        <select
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
        >
          <option value="">Select a user</option>

          {users.map((user) => (
            <option
              key={user.user_id}
              value={user.user_id}
            >
              {user.username}
            </option>
          ))}
        </select>

        <br />
        <br />

        <label>Order Description</label>

        <textarea
          value={description}
          onChange={(e) =>
            setDescription(e.target.value)
          }
          placeholder="Enter order description..."
        />

        <br />

        <button onClick={createOrder}>
          Create Order
        </button>

        {message && <p>{message}</p>}
      </div>

      {/* ORDERS */}
      <div className="card">
        <h2>Orders</h2>

        {orders.length === 0 ? (
          <p>No orders found.</p>
        ) : (
          <table>
            <thead>
              <tr>
                <th>Order ID</th>
                <th>User ID</th>
                <th>Description</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>
              {orders.map((order) => (
                <tr key={order.order_id}>
                  <td>{order.order_id}</td>

                  <td>{order.user_id}</td>

                  <td>{order.description}</td>

                  <td>{order.order_status}</td>

                  <td>
                    {order.order_status !== "COMPLETED" && (
                      <button
                        onClick={() =>
                          processOrder(order.order_id)
                        }
                        disabled={
                          processingOrderId ===
                          order.order_id
                        }
                      >
                        {processingOrderId ===
                        order.order_id
                          ? "Processing..."
                          : "Process"}
                      </button>
                    )}

                    {order.order_status === "COMPLETED" && (
                      <button
                        onClick={() =>
                          getProcessedOrder(
                            order.order_id
                          )
                        }
                      >
                        View Result
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* AI PROCESSING RESULT */}
      {processedOrder && (
        <div className="card result">
          <h2>AI Processing Result</h2>

          <p>
            <strong>Order ID:</strong>{" "}
            {processedOrder.order_id}
          </p>

          <h3>Items</h3>

          {processedOrder.extracted_data.items.map(
            (item, index) => (
              <div key={index}>
                <p>
                  <strong>Name:</strong>{" "}
                  {item.name}
                </p>

                <p>
                  <strong>Quantity:</strong>{" "}
                  {item.quantity}
                </p>

                <p>
                  <strong>Size:</strong>{" "}
                  {item.size || "Not specified"}
                </p>
              </div>
            )
          )}

          <p>
            <strong>Delivery Address:</strong>{" "}
            {processedOrder.extracted_data
              .delivery_address ||
              "Not specified"}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;