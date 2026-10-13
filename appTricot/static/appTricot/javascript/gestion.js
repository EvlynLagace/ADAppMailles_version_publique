function GestionEchantillon() {
    const [ouvert, setOuvert ] = React.useState(false);
    const [nom, setNom ] = React.useState("Mon échantillon");
    const [echantillons, setEchantillons] = React.useState([])

    React.useEffect(() => {
        if (!ouvert) {
            return;
        }

        fetch("/appTricot/api/echantillons/")
            .then(res => res.json())
            .then(data => setEchantillons(data.echantillons));
    }, [ouvert]);

    function ouvrir() {
        setOuvert(true);
    }

    function fermer() {
        setOuvert(false);
    }

    async function sauvegarder(){
        const formData = new FormData();
        formData.append("nom_echantillon", nom);

        const response = await fetch(
            "/appTricot/sauvegarder_echantillon_compte/",
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok) {
            setOuvert(false);
        }
    }

    async function recupererEchantillon(echantillonId) {
        const formData = new FormData();
        formData.append("echantillon_id", echantillonId);

        const response = await fetch(
            "/appTricot/recuperer_echantillon_compte/",
            {
                method:"POST",
                headers: {
                    "X-CSRFToken":getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok){
            window.location.href = "/appTricot/couverture/";
        }
    }

    async function supprimerEchantillon(echantillonId) {
        const formData = new FormData();
        formData.append("echantillon_id", echantillonId);

        const response = await fetch(
            "/appTricot/supprimer_echantillon_compte/",
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok){
            window.location.href = "/appTricot/couverture/";
        }
    }

    if(ouvert) {
        return e(
            "div",
            { className: "dialogue-gestion"},
        
            e(
                "h3",
                null,
                "Liste de vos échantillons"
            ),

            e(
                "ul",
                null,

                echantillons.map((echantillon)=>
                    e(
                        "li",
                        {key: echantillon.id},
                        echantillon.nom,
                        " - ",
                        `${echantillon.nb_mailles} mailles × ${echantillon.nb_rangs} rangs`,
                        " - ",
                        `${echantillon.largeur_cm} × ${echantillon.hauteur_cm} cm`,
                        e(
                            "div",
                            { className:"actions-gestion" },
                            e(
                                "a",
                                {
                                    href:"#",
                                    onClick: (event) => {
                                        event.preventDefault();
                                        recupererEchantillon(echantillon.id);
                                    }
                                },
                                "Récupérer"
                            ),
                            e(
                                "a",
                                {
                                    href:"#",
                                    onClick: (event)=> {
                                        event.preventDefault();
                                        supprimerEchantillon(echantillon.id);
                                    }
                                },
                                "Effacer"
                            )
                        )
                    )
                )
            ),         

                  
            e(
                "button",
                {
                    className: "bouton",
                    onClick: fermer
                },
                "Annuler"
            ),


        );
    }

    return e(
        "button",
        {
            className: "bouton",
            onClick: ouvrir
        },
        "Gérer les échantillons"
    )
}

function GestionCouverture() {
    const [ouvert, setOuvert ] = React.useState(false);
    const [couvertures, setCouvertures] = React.useState([])

    React.useEffect(() => {
        if (!ouvert) {
            return;
        }

        fetch("/appTricot/api/couvertures/")
            .then(res => res.json())
            .then(data => setCouvertures(data.couvertures));
    }, [ouvert]);

    function ouvrir() {
        setOuvert(true);
    }

    function fermer() {
        setOuvert(false);
    }

    async function recupererCouverture(couvertureId) {
        const formData = new FormData();
        formData.append("couverture_id", couvertureId);

        const response = await fetch(
            "/appTricot/recuperer_couverture_compte/",
            {
                method:"POST",
                headers: {
                    "X-CSRFToken":getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok){
            window.location.href = "/appTricot/couverture/";
        }
    }

    async function supprimerCouverture(couvertureId) {
        const formData = new FormData();
        formData.append("couverture_id", couvertureId);

        const response = await fetch(
            "/appTricot/supprimer_couverture_compte/",
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok){
            window.location.href = "/appTricot/couverture/";
        }
    }

    if (ouvert) {
        return e(
            "div",
            { className:"dialogue-gestion"},

            e(
                "h3",
                null,
                "Liste de vos couvertures"
            ),

            e(
                "ul",
                null,

                couvertures.map((couverture)=>
                    e(
                        "li",
                        { key: couverture.id },
                        couverture.nom,
                        " - ",
                        `${couverture.largeur_cm} × ${couverture.hauteur_cm} cm`,
                        e(
                            "div",
                            { className:"actions-gestion" },
                            e(
                                "a",
                                {
                                    href:"#",
                                    onClick: (event) => {
                                        event.preventDefault();
                                        recupererCouverture(couverture.id);
                                    }
                                },
                                "Récupérer"
                            ),
                            e(
                                "a",
                                {
                                    href:"#",
                                    onClick: (event) => {
                                        event.preventDefault();
                                        supprimerCouverture(couverture.id);
                                    }
                                    
                                },
                                "Effacer"
                            )
                        )
                    )
                )
            ),

            e(
                "button",
                {
                    className:"bouton",
                    onClick: fermer
                },
                "Annuler"
            )
        );
    }

    return e(
        "button",
        {
            className: "bouton",
            onClick: ouvrir
        },
        "Gérer les couvertures"
    );
}

function SauvegardeCouverture() {
    const [nom, setNom ] = React.useState("Ma couverture");

    async function sauvegarder(){
        const formData = new FormData();
        formData.append("nom_couverture", nom);

        const response = await fetch(
            "/appTricot/sauvegarder_couverture_compte/",
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok) {
            window.location.href = "/appTricot/couverture/";
}
    }

    return e(
        "div",
        null,

        e(
            "label",
            { htmlFor: "nom-couverture" },
            "Nom de la couverture : "
        ),

        e(
            "input",
            {
                type: "text",
                id: "nom-couverture",
                name: "nom_couverture",
                value: nom,
                onChange: (event) => setNom(event.target.value)
            }
        ),

        e(
            "button",
            {
                className: "bouton",
                onClick: sauvegarder
            },
            "Sauvegarder"
        )
    );
}

function SauvegardeEchantillon() {
    const [nom, setNom ] = React.useState("Mon échantillon");

    async function sauvegarder(){
        const formData = new FormData();
        formData.append("nom_echantillon", nom);

        const response = await fetch(
            "/appTricot/sauvegarder_echantillon_compte/",
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            }
        );

        if (response.ok) {
            window.location.href = "/appTricot/couverture/";
}
    }

    return e(
        "div",
        null,

        e(
            "label",
            { htmlFor: "nom-echantillon" },
            "Nom de l'échantillon : "
        ),

        e(
            "input",
            {
                type: "text",
                id: "nom-echantillon",
                name: "nom_echantillon",
                value: nom,
                onChange: (event) => setNom(event.target.value)
            }
        ),

        e(
            "button",
            {
                className: "bouton",
                onClick: sauvegarder
            },
            "Sauvegarder"
        )
    );
}

ReactDOM.createRoot(
    document.getElementById('react-gestion-echantillon')
).render(
    e(GestionEchantillon)
);

ReactDOM.createRoot(
    document.getElementById('react-gestion-couverture')
).render(
    e(GestionCouverture)
);

ReactDOM.createRoot(
    document.getElementById('react-sauvegarde-couverture')
).render(
    e(SauvegardeCouverture)
);

ReactDOM.createRoot(
    document.getElementById('react-sauvegarde-echantillon')
).render(
    e(SauvegardeEchantillon)
);