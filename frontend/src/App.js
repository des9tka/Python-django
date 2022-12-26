import {useEffect, useState} from "react";
import axios from "axios";

function App() {
    const [cars, setCars] = useState([])
    useEffect(() => {
        axios.get('/api/cars').then(value => setCars(value.data))
    }, [])
    return(
        <div>
            <h1>Cars</h1>
            {cars.map(car => <div>car_brand - {car.car_brand}</div>)}
        </div>
    )
}

export default App;
