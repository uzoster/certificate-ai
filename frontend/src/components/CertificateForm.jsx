import { useState } from "react";
import api from "../services/api";

function CertificateForm() {

    const [form, setForm] = useState({
        fullname: "",
        course: "",
        trainer: "",
        background: "gold.jpg"
    });

    const [loading, setLoading] = useState(false);
    const [certificate, setCertificate] = useState(null);

    const handleChange = (e) => {

        setForm({
            ...form,
            [e.target.name]: e.target.value
        });

    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const res = await api.post("/certificate/", form);

            setCertificate(res.data);

            alert("Certificate created!");

        } catch (err) {

            console.log(err);

            alert("Server Error");

        }

        setLoading(false);

    };

    return (

        <div
            style={{
                background: "#fff",
                padding: 30,
                borderRadius: 10,
                boxShadow: "0 0 10px rgba(0,0,0,.1)"
            }}
        >

            <form onSubmit={handleSubmit}>

                <input
                    type="text"
                    name="fullname"
                    placeholder="Full Name"
                    value={form.fullname}
                    onChange={handleChange}
                    style={input}
                />

                <input
                    type="text"
                    name="course"
                    placeholder="Course"
                    value={form.course}
                    onChange={handleChange}
                    style={input}
                />

                <input
                    type="text"
                    name="trainer"
                    placeholder="Trainer"
                    value={form.trainer}
                    onChange={handleChange}
                    style={input}
                />

                <select
                    name="background"
                    value={form.background}
                    onChange={handleChange}
                    style={input}
                >
                    <option value="gold.jpg">
                        Gold
                    </option>
                </select>

                <button
                    type="submit"
                    style={button}
                >

                    {loading ? "Generating..." : "Generate Certificate"}

                </button>

            </form>

            {certificate && (

                <div
                    style={{
                        marginTop:30
                    }}
                >

                    <h2>Certificate Created</h2>

                    <p><b>ID:</b> {certificate.id}</p>

                    <p><b>UUID:</b> {certificate.uuid}</p>

                    <p><b>Name:</b> {certificate.fullname}</p>

                    <p><b>Course:</b> {certificate.course}</p>

                    <p><b>Trainer:</b> {certificate.trainer}</p>

                </div>

            )}

        </div>

    );

}

const input={

    width:"100%",
    padding:"12px",
    marginBottom:"15px",
    border:"1px solid #ddd",
    borderRadius:"8px",
    fontSize:"16px"

}

const button={

    width:"100%",
    padding:"14px",
    background:"#2563eb",
    color:"#fff",
    border:"none",
    borderRadius:"8px",
    cursor:"pointer",
    fontSize:"16px"

}

export default CertificateForm;