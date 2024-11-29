import React, { useState } from "react";
import axios from "axios";
import { API_BASE_URL } from "../config";

const GetSchedulableSlots = () => {
  const [candidateId, setCandidateId] = useState("");
  const [interviewerId, setInterviewerId] = useState("");
  const [slots, setSlots] = useState([]);

  const handleFetchSlots = async () => {
    try {
      const response = await axios.get(
        `${API_BASE_URL}/get-schedulable-slots/`,
        { params: { candidate_id: candidateId, interviewer_id: interviewerId } }
      );
      setSlots(response.data.schedulable_slots || []);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch schedulable slots. Please check the IDs.");
    }
  };

  return (
    <div>
      <h2>Get Schedulable Slots</h2>
      <label>
        Candidate ID:
        <input type="number" value={candidateId} onChange={(e) => setCandidateId(e.target.value)} />
      </label>
      <br />
      <label>
        Interviewer ID:
        <input type="number" value={interviewerId} onChange={(e) => setInterviewerId(e.target.value)} />
      </label>
      <br />
      <button onClick={handleFetchSlots}>Fetch Slots</button>
      <div>
        <h3>Available Slots:</h3>
        <ul>
          {slots.map((slot, index) => (
            <li key={index}>{slot[0]} - {slot[1]}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default GetSchedulableSlots;
