/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_has_duplicates.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 05:40:32 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/01 23:13:05 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_has_duplicates(t_stack *stack)
{
	t_stack	*current;
	t_stack	*checker;

	current = stack->next;
	while (current != stack)
	{
		checker = current->next;
		while (checker != current)
		{
			if (current->nbr == checker->nbr)
				return (1);
			checker = checker->next;
		}
		current = current->next;
	}
	return (0);
}
