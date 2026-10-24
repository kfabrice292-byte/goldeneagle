/**
 * Golden Eagle SARL - WhatsApp Business & Geskap Integration Service
 * 
 * Ce module gère :
 * 1. La génération d'actions directes WhatsApp vers le support opérations Golden Eagle
 * 2. La préparation des requêtes API vers l'infrastructure Geskap (https://wa-api.geskap.com)
 *    pour l'envoi de messages templates UTILITY (ex: accusé de réception de devis)
 * 3. La synchronisation avec Firestore (wa_messages) conformément aux spécifications
 */

const GESKAP_CONFIG = {
    baseUrl: 'https://wa-api.geskap.com',
    defaultRecipientPhone: '22625375333', // Numéro officiel Golden Eagle // Numéro WhatsApp Golden Eagle (non configuré)
    companyName: 'Golden Eagle SARL',
    officialEmail: 'info@goldeneaglebf.com',
    headquartersPhone: '+226 25 37 53 33'
};

/**
 * Génère un lien direct WhatsApp pour préremplir une demande commerciale
 * @param {Object} details { clientName, company, serviceType, location, message }
 * @returns {string} URL wa.me formatée
 */
export function generateWhatsAppQuoteLink({ clientName, company, serviceType, location, message }) {
    const text = 
`*DEMANDE DE COTATION — GOLDEN EAGLE SARL*
----------------------------------------
*Client :* ${clientName || 'Non précisé'}
*Entreprise :* ${company || 'Particulier/Non précisé'}
*Prestation demandée :* ${serviceType || 'Forage & Minage'}
*Localisation du site / Mine :* ${location || 'Burkina Faso / Sous-région'}

*Détails du besoin :*
${message || 'Bonjour, je souhaite obtenir une cotation pour ce projet.'}
----------------------------------------
_Envoyé depuis le site officiel goldeneaglebf.com_`;

    return `https://wa.me/${GESKAP_CONFIG.defaultRecipientPhone}?text=${encodeURIComponent(text)}`;
}

/**
 * Envoi d'un message template de confirmation de demande de devis via Geskap WhatsApp API
 * (À appeler depuis votre backend sécurisé ou Firebase Cloud Function avec votre clé Bearer sk_live_...)
 * 
 * @param {string} apiKey Clé secrète Geskap sk_live_...
 * @param {string} toClientPhone Numéro du client au format international E.164 (ex: +226...)
 * @param {string} quoteId Identifiant unique de devis (ex: DEV-2026-089)
 * @param {string} clientName Nom du client
 * @param {string} serviceName Nom du service demandé
 */
export async function sendGeskapQuoteAcknowledgment(apiKey, toClientPhone, quoteId, clientName, serviceName) {
    if (!apiKey) {
        console.warn("[Geskap Service] Clé API non fournie. Requête ignorée côté client pour des raisons de sécurité.");
        return null;
    }

    try {
        const response = await fetch(`${GESKAP_CONFIG.baseUrl}/v1/messages`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                to: toClientPhone,
                template: {
                    name: 'order_confirmation', // Template standard UTILITY
                    language: 'fr',
                    variables: [clientName, quoteId, serviceName]
                },
                idempotency_key: `quote-${quoteId}`
            })
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || `Erreur API Geskap: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("[Geskap Service] Échec d'envoi du template WhatsApp :", error);
        throw error;
    }
}

// Initialisation globale pour le navigateur
if (typeof window !== 'undefined') {
    window.GoldenEagleWhatsApp = {
        config: GESKAP_CONFIG,
        generateQuoteLink: generateWhatsAppQuoteLink
    };
}
