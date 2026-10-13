const e = React.createElement;

//Helpers
function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');

        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }

    return cookieValue;
}

//Fonctions API
async function getMotifsCompatibles (i, j) {
    const res = await fetch(
        `/appTricot/api/tuile/${i}/${j}/motif/`
    );

    if (!res.ok) {
        throw new Error("Erreur serveur");
    }

    return await res.json();
}

async function setMotif(i, j, nomMotif){
    const formData = new FormData();
    formData.append("nom_motif", nomMotif);

    const res = await fetch(
        `/appTricot/api/tuile/${i}/${j}/motif/`,
        {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: formData
        }
    );

    const data = await res.json();

    if (!res.ok) {
        throw new Error("Erreur serveur");
    }

    return data;
}

//hooks

function useCouverture(){
    const [couverture, setCouverture] = React.useState(null);

    React.useEffect(() => {
        fetch("/appTricot/api/couverture/")
            .then(res => res.json())
            .then(data => setCouverture(data));
    }, []);

    return[couverture, setCouverture]
}

function useMenu(){
    const [menu, setMenu] = React.useState(null); 

    React.useEffect(() => {

        function fermerMenu(event) {

            // ❗ ne pas fermer si on clique dans le menu
            if (event.target.closest(".menu-contextuel")) {
                return;
            }

            setMenu(null);
        }

        document.addEventListener("click", fermerMenu);

        return () => {
            document.removeEventListener("click", fermerMenu);
        };

    }, []);

    return [menu, setMenu];
}

//Composants
function Tuile({ tuile, i, j, onOpenMenu, grilleRef }) {

    function handleClick(event){
        event.preventDefault();
        event.stopPropagation();

        const rect = event.currentTarget.getBoundingClientRect();
        const grille = grilleRef.current.getBoundingClientRect();
        console.log("grilleRef", grilleRef.current);

        onOpenMenu({
            x: rect.right - grille.left + 10,
            y: rect.top - grille.top,
            i,
            j,
            tuile,
            mode:"actions"
        });
    }

    return e(
        "div",
        {
            className: "tuile",
            onClick: handleClick,
            style: {
                "--couleur-motif": tuile.motif.couleur_motif,
            }
        },
        tuile.motif.nom_motif
    )
}

function MenuContextuel({ menu, onClose, setMenu, setCouverture }) {

    if (!menu) return null;

    function voirTuile() {
         window.open(`/appTricot/tuile/${menu.i}/${menu.j}`, '_blank');
    }

    async function modifierMotif() {
        const data = await getMotifsCompatibles(menu.i, menu.j);

        setMenu({
            ...menu,
            mode: "motifs",
            motifs: data.motifs
        });
    }

    async function choisirMotif(motif) {
        const data = await setMotif(menu.i, menu.j, motif.nom_motif);

        if (data.ok) {

            // mise à jour locale (option recommandé)
            setCouverture(prev => {
                const copy = structuredClone(prev);
                copy.tuiles[menu.i][menu.j].motif = data.motif;
                return copy;
            });

            window.location.reload();
            setMenu(null);
        }
    }

    return e(
        "div",
        {
            className: "menu-contextuel",
            onClick: (e) => e.stopPropagation(),
            style: {
                left: menu.x,
                top: menu.y,
            }
        },

        /* =========================
           HEADER INFO
        ========================= */

        e("div", {
            className:"menu-contextuel-info"
        }, `Tuile (${menu.i + 1}, ${menu.j + 1})`),

        e("div", {
            className:"menu-contextuel-info"
        }, `Motif : ${menu.tuile.motif.nom_motif}`),

        e("img", {
            src: `/static/${menu.tuile.motif.photo}`,
            alt: menu.tuile.motif.nom_motif,
            className:"menu-contextuel-image"
        }),

        /* =========================
           MODE ACTIONS
        ========================= */

        menu.mode !== "motifs" && e(React.Fragment, null,

            e("div", {
                className:"menu-item",
                onClick: voirTuile,
            }, "👁 Voir les instructions"),

            e("div", {
                className:"menu-item",
                onClick: modifierMotif,
            }, "🎨 Modifier le motif")
        ),

        /* =========================
           MODE MOTIFS
        ========================= */

        menu.mode === "motifs" && e(React.Fragment, null,

            e("div", {
                className:"menu-contextuel-info"
            }, "Choisir un motif"),

            menu.motifs?.map(motif =>
                e("div", {
                    key: motif.nom_motif,
                    className:"menu-item",
                    onClick: () => choisirMotif(motif),
                }, motif.nom_motif)
            ),
        )
    );
}

//App
function App() {

    const [couverture, setCouverture] = useCouverture();
    const [menu, setMenu] = useMenu();
    const grilleRef = React.useRef(null);

    if (!couverture) {
        return e("div", null, "Chargement...");
    }

    function updateMotif(i, j, motif) {

        setCouverture(prev => {
            const copy = structuredClone(prev);
            copy.tuiles[i][j].motif = motif;
            return copy;
        });
    }

    return e(
        React.Fragment,
        null,

        e(
            "div",
            {className:"grille-couverture-react",
                ref:grilleRef
            },
            couverture.tuiles.map((ligne, i) =>
                e(
                    "div",
                    { key: i, style: { display: "flex" } },
                    ligne.map((tuile, j) =>
                        e(Tuile, {
                            key: j,
                            tuile,
                            i,
                            j,
                            onOpenMenu: setMenu,
                            grilleRef
                        })
                    )
                )
            )
        ),

        e(MenuContextuel, {
            menu,
            setMenu,
            setCouverture,
            onClose: () => setMenu(null),
        })
    );
}

//Render
ReactDOM.createRoot(
    document.getElementById("react-root")
).render(e(App));

// Chargement de fichier JSON

function initialiserChargementFichier(idBouton, idInput, idFormulaire) {

    const bouton = document.getElementById(idBouton);
    const input = document.getElementById(idInput);
    const formulaire = document.getElementById(idFormulaire);

    if (!bouton || !input || !formulaire) {
        return;
    }

    bouton.addEventListener("click", () => {
        input.click();
    });

    input.addEventListener("change", () => {
        if (input.files.length > 0) {
            formulaire.submit();
        }
    });
}

initialiserChargementFichier(
    "bouton-charger-couverture",
    "fichier_couverture",
    "form-charger-couverture"
);

initialiserChargementFichier(
    "bouton-charger-echantillon",
    "fichier_echantillon",
    "form-charger-echantillon"
);