document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("projectForm");
    const tableBody = document.getElementById("projectTableBody");
    const exportBtn = document.getElementById("exportCsv");

    // CREATE PROJECT (POST)
    if (form) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            const data = {
                project_code: form.project_code.value,
                client_name: form.client_name.value,
                country: form.country.value,
                cpi: parseFloat(form.cpi.value),
                loi: parseInt(form.loi.value, 10),
                status: form.status.value
            };
            try {
                const res = await fetch("/api/create-project", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });
                if (res.ok) {
                    alert("✅ Project Created!");
                    form.reset();
                    window.location.href = "/dashboard.html";
                } else {
                    alert("❌ Failed to create project.");
                }
            } catch (err) {
                console.error(err);
                alert("❌ Error connecting to backend.");
            }
        });
    }

    // LIST PROJECTS (GET)
    if (tableBody) {
        fetch("/api/projects")
            .then(res => res.json())
            .then(projects => {
                tableBody.innerHTML = projects.map(p => `
                    <tr>
                        <td>${p.project_code}</td>
                        <td>${p.client_name}</td>
                        <td>${p.country}</td>
                        <td>$${p.cpi.toFixed(2)}</td>
                        <td>${p.loi} min</td>
                        <td>${p.status}</td>
                        <td>
                            <button class="btn btn-sm btn-danger" onclick="deleteProject('${p.project_code}')">
                                <i class="fas fa-trash"></i> Delete
                            </button>
                        </td>
                    </tr>
                `).join('');
            });
    }

    // DELETE PROJECT
    window.deleteProject = async (code) => {
        if (!confirm(`Delete project ${code}?`)) return;
        const res = await fetch(`/api/projects/${code}`, { method: "DELETE" });
        if (res.ok) {
            alert("✅ Project deleted.");
            location.reload();
        } else {
            alert("❌ Failed to delete.");
        }
    };

    // EXPORT CSV
    if (exportBtn) {
        exportBtn.addEventListener("click", () => {
            fetch("/api/projects")
                .then(res => res.json())
                .then(data => {
                    let csv = "Project Code,Client Name,Country,CPI,LOI,Status\n";
                    data.forEach(p => {
                        csv += `${p.project_code},${p.client_name},${p.country},${p.cpi},${p.loi},${p.status}\n`;
                    });
                    const blob = new Blob([csv], { type: "text/csv" });
                    const a = document.createElement("a");
                    a.href = URL.createObjectURL(blob);
                    a.download = "projects.csv";
                    a.click();
                });
        });
    }
});
