import CertificateForm from "../components/CertificateForm";

function Dashboard(){

    return(

        <div
            style={{
                width:"900px",
                margin:"50px auto"
            }}
        >

            <h1
                style={{
                    marginBottom:"30px"
                }}
            >
                AI Certificate Studio
            </h1>

            <CertificateForm/>

        </div>

    )

}

export default Dashboard;