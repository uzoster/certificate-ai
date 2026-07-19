import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Certificates from "./pages/Certificates";
import Verify from "./pages/Verify";

function App() {
    return (
        <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/certificates" element={<Certificates />} />
            <Route path="/verify/:uuid" element={<Verify />} />
        </Routes>
    );
}

export default App;